import mysql.connector
from mysql.connector import Error
import mysql.connector
from mysql.connector import Error

try:
    # Establish connection to MySQL server
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234"  # 
    )

    # Cursor inside try to include CREATE DATABASE
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_BOOK_STORE")
    print("Database 'alx_book_store' created successfully!")

except Error as e:
    # Handle exceptions properly
    print(f"Error: {e}")

finally:
    # Properly close cursor and connection
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()

try:
    # Establish connection to MySQL server
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="YHWH_mypassword"  # Replace with your MySQL password
    )

    # CREATE DATABASE statement for ALX_BOOK_STORE
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_BOOK_STORE")
    print("Database 'alx_book_store' created successfully!")

except Error as e:
    # Handle exceptions if connection or creation fails
    print(f"Error: {e}")

finally:
    # Close cursor and connection properly
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
