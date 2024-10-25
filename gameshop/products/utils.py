import mysql.connector

def export_data():
    db = mysql.connector.connect(user='root', password='LalachkA007', host='localhost', database='gameshop')
    cursor = db.cursor()
    cursor.execute("SELECT * FROM products_game")
    data = cursor.fetchall()
    cursor.close()
    db.close()
    return data

def import_data(data):
    db = mysql.connector.connect(user='root', password='LalachkA007', host='localhost', database='gameshop')
    cursor = db.cursor()
    cursor.executemany("INSERT INTO products_game (title, description, price, category) VALUES (%s, %s, %s, %s)", data)
    db.commit()
    cursor.close()
    db.close()
