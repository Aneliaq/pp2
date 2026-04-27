import csv
import json
from connect import connect


# Add contact with multiple phone numbers
def insert_from_console():
    conn = connect()
    cur = conn.cursor()

    name = input("Name: ")
    email = input("Email: ")
    birthday = input("Birthday (YYYY-MM-DD): ")
    group_name = input("Group (Family/Work/Friend): ")

    # Create or get group
    cur.execute("SELECT id FROM groups WHERE name = %s", (group_name,))
    group = cur.fetchone()

    if group is None:
        cur.execute(
            "INSERT INTO groups(name) VALUES (%s) RETURNING id",
            (group_name,)
        )
        group_id = cur.fetchone()[0]
    else:
        group_id = group[0]

    # Insert contact
    cur.execute(
        "INSERT INTO contacts(name, email, birthday, group_id) VALUES (%s, %s, %s, %s) RETURNING id",
        (name, email, birthday, group_id)
    )
    contact_id = cur.fetchone()[0]

    # Add multiple phones
    while True:
        phone = input("Phone: ")
        p_type = input("Type (home/work/mobile): ")

        cur.execute(
            "INSERT INTO phones(contact_id, phone, type) VALUES (%s, %s, %s)",
            (contact_id, phone, p_type)
        )

        more = input("Add another phone? (y/n): ")
        if more.lower() != 'y':
            break

    conn.commit()
    cur.close()
    conn.close()
    print("Contact added!")


# CSV import
def insert_from_csv():
    conn = connect()
    cur = conn.cursor()

    with open('contacts.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row['name']
            phone = row['phone']

            cur.execute(
                "INSERT INTO contacts (name) VALUES (%s) RETURNING id",
                (name,)
            )
            contact_id = cur.fetchone()[0]

            cur.execute(
                "INSERT INTO phones (contact_id, phone, type) VALUES (%s, %s, %s)",
                (contact_id, phone, 'mobile')
            )

    conn.commit()
    cur.close()
    conn.close()
    print("CSV imported!")


# Search (DB function: name, phone, email)
def search():
    pattern = input("Search: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM search_contacts(%s::text);", (pattern,))
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()


# Search by email only
def search_by_email():
    email = input("Email search: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM contacts WHERE email ILIKE %s",
        ('%' + email + '%',)
    )

    for row in cur.fetchall():
        print(row)

    cur.close()
    conn.close()


# Filter by group
def filter_by_group():
    group_name = input("Group: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        SELECT c.name, c.email, p.phone
        FROM contacts c
        JOIN groups g ON c.group_id = g.id
        LEFT JOIN phones p ON c.id = p.contact_id
        WHERE g.name = %s
    """, (group_name,))

    for row in cur.fetchall():
        print(row)

    cur.close()
    conn.close()


# Sort contacts
def sort_contacts():
    field = input("Sort by (name/birthday/created): ")

    if field == "name":
        order = "c.name"
    elif field == "birthday":
        order = "c.birthday"
    else:
        order = "c.id"

    conn = connect()
    cur = conn.cursor()

    cur.execute(f"""
        SELECT c.name, c.email, c.birthday
        FROM contacts c
        ORDER BY {order}
    """)

    for row in cur.fetchall():
        print(f"Name: {row[0]} | Email: {row[1]} | Birthday: {row[2]}")

    cur.close()
    conn.close()


# Pagination
def pagination():
    limit = int(input("Limit: "))
    offset = 0

    while True:
        conn = connect()
        cur = conn.cursor()

        cur.execute(
            "SELECT * FROM get_contacts_paginated(%s, %s);",
            (limit, offset)
        )

        for row in cur.fetchall():
            print(row)

        cur.close()
        conn.close()

        cmd = input("n-next, p-prev, q-quit: ")

        if cmd == 'n':
            offset += limit
        elif cmd == 'p':
            offset = max(0, offset - limit)
        elif cmd == 'q':
            break


# Delete contact
def delete():
    value = input("Name or phone: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute("CALL delete_contact(%s);", (value,))
    conn.commit()

    cur.close()
    conn.close()
    print("Deleted!")


# Export JSON
def export_json():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        SELECT c.name, c.email, c.birthday, g.name, p.phone, p.type
        FROM contacts c
        LEFT JOIN groups g ON c.group_id = g.id
        LEFT JOIN phones p ON c.id = p.contact_id
    """)

    data = []
    for row in cur.fetchall():
        data.append({
            "name": row[0],
            "email": row[1],
            "birthday": str(row[2]),
            "group": row[3],
            "phone": row[4],
            "type": row[5]
        })

    with open("contacts.json", "w") as f:
        json.dump(data, f, indent=4)

    cur.close()
    conn.close()
    print("Exported!")


# Import JSON with duplicate handling
def import_json():
    conn = connect()
    cur = conn.cursor()

    with open("contacts.json", "r") as f:
        data = json.load(f)

    for item in data:
        name = item["name"]

        cur.execute("SELECT id FROM contacts WHERE name = %s", (name,))
        existing = cur.fetchone()

        if existing:
            choice = input(f"{name} exists (s=skip/o=overwrite): ")
            if choice == "s":
                continue
            else:
                cur.execute("DELETE FROM contacts WHERE name = %s", (name,))

        group_name = item["group"]

        cur.execute("SELECT id FROM groups WHERE name = %s", (group_name,))
        group = cur.fetchone()

        if group is None:
            cur.execute(
                "INSERT INTO groups(name) VALUES (%s) RETURNING id",
                (group_name,)
            )
            group_id = cur.fetchone()[0]
        else:
            group_id = group[0]

        cur.execute(
            "INSERT INTO contacts(name, email, birthday, group_id) VALUES (%s, %s, %s, %s) RETURNING id",
            (item["name"], item["email"], item["birthday"], group_id)
        )
        contact_id = cur.fetchone()[0]

        cur.execute(
            "INSERT INTO phones(contact_id, phone, type) VALUES (%s, %s, %s)",
            (contact_id, item["phone"], item["type"])
        )

    conn.commit()
    cur.close()
    conn.close()
    print("Imported JSON!")


# Menu
def menu():
    while True:
        print("\n1. CSV import")
        print("2. Console insert")
        print("3. Search")
        print("4. Search by email")
        print("5. Filter by group")
        print("6. Sort")
        print("7. Pagination")
        print("8. Delete")
        print("9. Export JSON")
        print("10. Import JSON")
        print("0. Exit")

        choice = input("Choose: ")

        if choice == "1":
            insert_from_csv()
        elif choice == "2":
            insert_from_console()
        elif choice == "3":
            search()
        elif choice == "4":
            search_by_email()
        elif choice == "5":
            filter_by_group()
        elif choice == "6":
            sort_contacts()
        elif choice == "7":
            pagination()
        elif choice == "8":
            delete()
        elif choice == "9":
            export_json()
        elif choice == "10":
            import_json()
        elif choice == "0":
            break


menu()