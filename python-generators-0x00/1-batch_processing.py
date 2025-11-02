#!/usr/bin/python3

import mysql.connector
from mysql.connector import Error


def stream_users_in_batches(batch_size):
    """
Generator that fetches users from the database in batches.
Each yield returns a list of user dictionaries.
    """
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  
            database="ALX_prodev"
        )
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM user_data")

        while True:
            batch = cursor.fetchmany(batch_size)
            if not batch:
                break
            yield batch

    except Error as e:
        print(f"Error while fetching data in batches: {e}")

    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()


def batch_processing(batch_size):
    """
Processes batches of users to filter those over age 25.
Prints the filtered users.
    """
    for batch in stream_users_in_batches(batch_size):  # Loop 1
        for user in batch:  # Loop 2
            if user["age"] > 25:
                print(user)
                yield user
