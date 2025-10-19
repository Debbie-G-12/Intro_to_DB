import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password"  # replace with your MySQL password
    )

    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_BOOK_STORE")
    print("Database 'alx_book_store' created successfully!")

except Error as e:
    print(f"Error: {e}")

finally:
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
