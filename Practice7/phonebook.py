import csv
from connect import connect

def insert_from_csv():
    conn = connect()
    cur = conn.cursor()

    with open('contacts.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            cur.execute(
                "INSERT INTO contacts (name, phone) VALUES (%s, %s)",
                (row['name'], row['phone'])
            )

    conn.commit()
    cur.close()
    conn.close()
    print("CSV data inserted!")

def insert_from_console():
    name = input("Enter name: ")
    phone = input("Enter phone: ")

    conn = connect()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO contacts (name, phone) VALUES (%s, %s)",
        (name, phone)
    )
    conn.commit()
    cur.close()
    conn.close()
    print(f"{name} added!")


def update_contact():
    name = input("Enter name to update: ")
    new_phone = input("Enter new phone: ")

    conn = connect()
    cur = conn.cursor()
    cur.execute(
        "UPDATE contacts SET phone = %s WHERE name = %s",
        (new_phone, name)
    )
    conn.commit()
    cur.close()
    conn.close()
    print(f"{name} updated!")


def search_by_name():
    name = input("Enter name to search: ")

    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM contacts WHERE name = %s", (name,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()

def search_by_prefix():
    prefix = input("Enter phone prefix: ")

    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM contacts WHERE phone LIKE %s", (prefix+'%',))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()


def delete_contact():
    name = input("Enter name to delete: ")

    conn = connect()
    cur = conn.cursor()
    cur.execute("DELETE FROM contacts WHERE name = %s", (name,))
    conn.commit()
    cur.close()
    conn.close()
    print(f"{name} deleted!")


def menu():
    while True:
        print("\n1. Insert from CSV")
        print("2. Insert from console")
        print("3. Update contact")
        print("4. Search by name")
        print("5. Search by prefix")
        print("6. Delete contact")
        print("0. Exit")

        choice = input("Choose: ")
        if choice == "1": insert_from_csv()
        elif choice == "2": insert_from_console()
        elif choice == "3": update_contact()
        elif choice == "4": search_by_name()
        elif choice == "5": search_by_prefix()
        elif choice == "6": delete_contact()
        elif choice == "0": break

menu()