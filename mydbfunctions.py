import mysql.connector

def mydb():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Mxcitas0919",
        database="loto7_db"
    )
    return db
