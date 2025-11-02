#!/usr/bin/python3

import mysql.connector
from mysql.connector import Error
import csv
import uuid


def connect_db():
    """Connects to the MySQL database server...!!!"""
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password=""
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None


def create_database(connection):
    """Creates the ALX_prodev database if it doesn't exist...!!!"""
    try:
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev;")
        print("Database ALX_prodev created or already exists.")
    except Error as e:
        print(f"Error creating database: {e}")
    finally:
        cursor.close()


def connect_to_prodev():
    """Connects to the ALX_prodev database...!!!"""
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="ALX_prodev"
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error connecting to ALX_prodev: {e}")
        return None


def create_table(connection):
    """Creates the user_data table if it does not exist...!!!"""
    try:
        cursor = connection.cursor()
        create_table_query = """
CREATE TABLE IF NOT EXISTS user_data (
user_id CHAR(36) PRIMARY KEY,
name VARCHAR(255) NOT NULL,
email VARCHAR(255) NOT NULL,
age DECIMAL(3, 0) NOT NULL,
INDEX (user_id)
);
        """
        cursor.execute(create_table_query)
        connection.commit()
        print("Table user_data created successfully")
    except Error as e:
        print(f"Error creating table: {e}")
    finally:
        cursor.close()


def insert_data(connection, csv_file):
    """Inserts data from CSV file into user_data table...!!!"""
    try:
        cursor = connection.cursor()
        with open(csv_file, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                user_id = str(uuid.uuid4())
                name = row['name']
                email = row['email']
                age = row['age']

                # Insert only if email doesn’t already exist
                cursor.execute("SELECT * FROM user_data WHERE email = %s", (email,))
                exists = cursor.fetchone()
                if not exists:
                    cursor.execute(
                        "INSERT INTO user_data (user_id, name, email, age) VALUES (%s, %s, %s, %s)",
                        (user_id, name, email, age)
                    )

        connection.commit()
        print("Data inserted successfully")
    except Error as e:
        print(f"Error inserting data: {e}")
    except FileNotFoundError:
        print(f"Error: CSV file '{csv_file}' not found.")
    finally:
        cursor.close()
