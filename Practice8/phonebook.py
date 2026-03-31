from connect import get_connection

def search(pattern):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM search_contacts(%s);", (pattern,))
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()


def add_or_update(name, phone):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("CALL upsert_contact(%s, %s);", (name, phone))
    conn.commit()

    cur.close()
    conn.close()


def delete(value):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("CALL delete_contact(%s);", (value,))
    conn.commit()

    cur.close()
    conn.close()


def pagination(limit, offset):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM get_contacts_paginated(%s, %s);", (limit, offset))
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()


if __name__ == "__main__":
    print("Search:")
    search("Aig")

    print("\nAdd/Update:")
    add_or_update("Aliya", "+77012345678")

    print("\nPagination:")
    pagination(3, 0)

    print("\nDelete:")
    delete("Aliya")