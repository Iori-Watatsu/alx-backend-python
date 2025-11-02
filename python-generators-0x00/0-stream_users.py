#!/usr/bin/python3

import mysql.connector
from mysql.connector import Error


def stream_users():
    """Generator that yields user records from the user_data table one by one...!!!"""
    try:
        # Connect to the ALX_prodev database
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  
            database="ALX_prodev"
        )

        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM user_data")

        # Use only one loop
        for row in cursor:
            yield row

    except Error as e:
        print(f"Error while streaming data: {e}")

    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()
