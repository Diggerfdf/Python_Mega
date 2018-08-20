import psycopg2


def create_table():
    conn = psycopg2.connect("dbname = 'pymegatest' user='digger' password = 'mnemosine' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()


def insert(item, quantity, price):
    conn = psycopg2.connect("dbname = 'pymegatest' user='digger' password = 'mnemosine' host='localhost' port='5432'")
    cur = conn.cursor()
    # cur.execute("INSERT INTO store VALUES('%s', '%s', '%s')" % (item, quantity, price))
    cur.execute("INSERT INTO store VALUES(%s, %s, %s)", (item, quantity, price))
    conn.commit()
    conn.close()


def view():
    conn = psycopg2.connect("dbname = 'pymegatest' user='digger' password = 'mnemosine' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(item):
    conn = psycopg2.connect("dbname = 'pymegatest' user='digger' password = 'mnemosine' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item =%s", (item, ))
    conn.commit()
    conn.close()


def update(item, quantity, price):
    conn = psycopg2.connect("dbname = 'pymegatest' user='digger' password = 'mnemosine' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s", (quantity, price, item))
    conn.commit()
    conn.close()


# create_table()
# update("Pencil", 23, 5.9)
# insert("Wine Glass", 8, 10.5)
# insert("Coffee Cup", 10, 5.0)

# delete("Wine Glass")
# delete("Coffee Cup")
# delete("Strawberry")

update("Apple", 20, 16.1)
print(view())
