import sqlite3


def my_store_app():

    # This function check if we already have a databas. If we dont have it, it will ceate one.
    def create_table():
        conn = sqlite3.connect("lite.db")
        cur = conn.cursor()
        cur.execute(
            "CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")

        conn.commit()
        conn.close()

    # This funcion lets us view our items in the database
    def view_all_items():
        conn = sqlite3.connect("lite.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM store")
        rows = cur.fetchall()
        conn.close()
        print(rows)
        return rows

    # This fnction lets us insert new items in the database. Function recieve 3 parameter
    def insert_data(item, quantity, price):
        conn = sqlite3.connect("lite.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO store VALUES (?,?,?)",
                    (item, quantity, price))
        conn.commit()
        conn.close()

    # This function lets us update existing items in the database. Function recieve 3 parameter
    def update_item(quantity, price, item):
        conn = sqlite3.connect("lite.db")
        cur = conn.cursor()
        cur.execute("UPDATE store SET quantity=?, price=? WHERE item=?",
                    (quantity, price, item))
        conn.commit()
        conn.close()

    # This function lets us delete item in the database. We have to pass in the item name as parameter when calling the function.
    def delete_item(item):
        conn = sqlite3.connect("lite.db")
        cur = conn.cursor()
        cur.execute("DELETE FROM store WHERE item=?", (item,))
        conn.commit()
        conn.close()

    # Calling the createtable function
    create_table()

    print('Welcome to my store App!')
    print('')
    print('')
    print('What would you want to do? Choose from options below.')
    print('Option(1): View items')
    print('Option(2): Add new items')
    print('Option(3): Update item')
    print('Option(4): Delete item')
    print('Option(5): Clean screen')
    print('Option(6): Exit app')
    print('')
    option = input('Enter option number for your choice: ')
    if option == '1':
        print('You just choose to view all items in the database.')
        view_all_items()
        print()
        print()

    elif option == '2':
        print('Add new item now.')
        item = input('Item name: ')
        quantity = input('Quantity: ')
        price = input('Price: ')
        insert_data(item, quantity, price)
        print('Just added a new item.')
        print('')
        print('')

    elif option == '3':
        print('Its time to update a item.')
        item = input('Enter item name you want to update: ')
        quantity = input('New quantity: ')
        price = input('New price: ')
        update_item(quantity, price, item)
        print('Item just updadted')
        print('')
        print('')

    elif option == '4':
        print('Which item are you deleting?')
        item = input('Enter item name you want to delete: ')
        answer = input(
            'Are you sure you want to delete this item? | yes or no: ')
        if answer == 'yes':
            delete_item(item)
            print('Item was successfully deleted!')
        else:
            my_store_app()

    elif option == '5':
        print('')
        print('')

    my_store_app()


my_store_app()
