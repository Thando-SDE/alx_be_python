import mysql.connector
from mysql.connector import Error

def create_database():
    """Create the alx_book_store database if it doesn't exist"""
    connection = None
    try:
        # Connect to MySQL server (without specifying a database)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Lerishbusiness1#"  # Use your MySQL password
        )
        
        if connection.is_connected():
            # Create a cursor to execute SQL commands
            cursor = connection.cursor()
            
            # Create database if it doesn't exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            
            print("Database 'alx_book_store' created successfully!")
            
    except Error as e:
        print(f"Error: {e}")
        
    finally:
        # Close the connection properly
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

# Run the function
if __name__ == "__main__":
    create_database()