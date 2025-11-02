#!/usr/bin/python3

import seed
from mysql.connector import Error


def stream_user_ages():
    """
Generator that yields user ages one by one from the user_data table.
    """
    try:
        connection = seed.connect_to_prodev()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT age FROM user_data")

        # Use a single loop to yield each age
        for row in cursor:
            yield row["age"]

    except Error as e:
        print(f"Error streaming ages: {e}")

    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()


def calculate_average_age():
    """
Consumes the stream_user_ages generator to compute average age.
Uses no more than one loop for calculation.
    """
    total_age = 0
    count = 0

    for age in stream_user_ages():  # Loop 2 (total loops = 2)
        total_age += age
        count += 1

    if count > 0:
        average_age = total_age / count
        print(f"Average age of users: {average_age:.2f}")
    else:
        print("No users found in the database.")
