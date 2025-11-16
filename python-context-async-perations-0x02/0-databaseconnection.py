import sqlite3

class DatabaseConnection:
    def __init__(self, db_file):
        self.db_file = db_file
        self.conn = None

    def __enter__(self):
        # Open the database connection
        self.conn = sqlite3.connect(self.db_file)
        return self.conn  # return the connection object

    def __exit__(self, exc_type, exc_value, traceback):
        # Ensure the connection is closed
        if self.conn:
            self.conn.close()
        # Return False to propagate exceptions, if any
        return False

# Using the custom context manager
with DatabaseConnection("users.db") as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    results = cursor.fetchall()
    print(results)
    