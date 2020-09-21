# pip install mysql-connector-python==8.0.11
import mysql.connector
from mysql.connector import Error


def my_store_app():
    def check_conn():
        try:
            connection = mysql.connector.connect(
                host='sql9.freemysqlhosting.net',
                database='sql9366716',
                user='sql9366716',
                password='Z3775PZre6')
            if connection.is_connected():
                db_Info = connection.get_server_info()
                print("Connected to MySQL Server version ", db_Info)
                cursor = connection.cursor()
                cursor.execute("select database();")
                record = cursor.fetchone()
                print("You're connected to database: ", record)

        except Error as e:
            print("Error while connecting to MySQL", e)
        finally:
            if (connection.is_connected()):
                cursor.close()
                connection.close()
                print("MySQL connection is closed")

    def create_table():
        conn = mysql.connector.connect(
            host='sql9.freemysqlhosting.net',
            database='sql9366716',
            user='sql9366716',
            password='Z3775PZre6')
        cur = conn.cursor()
        cur.execute(
            "CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")

        conn.commit()
        conn.close()

    def insert_data(item, quantity, price):
        conn = mysql.connector.connect(
            host='sql9.freemysqlhosting.net',
            database='sql9366716',
            user='sql9366716',
            password='Z3775PZre6')
        cur = conn.cursor()
        cur.execute("INSERT INTO store VALUES (%s,%s,%s)",
                    (item, quantity, price))
        conn.commit()
        conn.close()

    def view_all_items():
        conn = mysql.connector.connect(
            host='sql9.freemysqlhosting.net',
            database='sql9366716',
            user='sql9366716',
            password='Z3775PZre6')
        cur = conn.cursor()
        cur.execute("SELECT * FROM store")
        rows = cur.fetchall()
        conn.close()
        print(rows)
        return rows

    def update_item(quantity, price, item):
        conn = mysql.connector.connect(
            host='sql9.freemysqlhosting.net',
            database='sql9366716',
            user='sql9366716',
            password='Z3775PZre6')
        cur = conn.cursor()
        cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s",
                    (quantity, price, item))
        conn.commit()
        conn.close()

    def delete_item(item):
        conn = mysql.connector.connect(
            host='sql9.freemysqlhosting.net',
            database='sql9366716',
            user='sql9366716',
            password='Z3775PZre6')
        cur = conn.cursor()
        cur.execute("DELETE FROM store WHERE item=%s", (item,))
        conn.commit()
        conn.close()
    # Check if table already exist, if not create one
    create_table()

    print('Welcome to my store App!')
    print('App database is hosted on a external online msql server')
    print('')
    print('')
    print('What would you want to do? Choose from options below.')
    print('Option(1): Check database connection')
    print('Option(2): View items')
    print('Option(3): Add new items')
    print('Option(4): Update item')
    print('Option(5): Delete item')
    print('Option(6): Clean screen')
    print('Option(7): Exit app')
    print('')

    option = input('Enter option number for your choice: ')
    if option == '1':
        check_conn()
    if option == '2':
        print('You just choose to view all items in the database.')
        view_all_items()
        print()
        print()

    elif option == '3':
        print('Add new item now.')
        item = input('Item name: ')
        quantity = input('Quantity: ')
        price = input('Price: ')
        insert_data(item, quantity, price)
        print('Just added a new item.')
        print('')
        print('')

    elif option == '4':
        print('Its time to update a item.')
        item = input('Enter item name you want to update: ')
        quantity = input('New quantity: ')
        price = input('New price: ')
        update_item(quantity, price, item)
        print('Item just updadted')
        print('')
        print('')

    elif option == '5':
        print('Which item are you deleting?')
        item = input('Enter item name you want to delete: ')
        answer = input(
            'Are you sure you want to delete this item? | yes or no: ')
        if answer == 'yes':
            delete_item(item)
            print('Item was successfully deleted!')
        else:
            my_store_app()

    elif option == '6':
        print('')
        print('')

    elif option == '7':
        exit()

    my_store_app()


my_store_app()
