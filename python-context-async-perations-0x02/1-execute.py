import sqlite3

class ExecuteQuery:
    def __init__(self, db_file, query, params=None):
        self.db_file = db_file
        self.query = query
        self.params = params if params else ()
        self.conn = None
        self.results = None

    def __enter__(self):
        # Open the connection
        self.conn = sqlite3.connect(self.db_file)
        cursor = self.conn.cursor()
        # Execute the query
        cursor.execute(self.query, self.params)
        self.results = cursor.fetchall()
        return self.results  # return the results to the with-block

    def __exit__(self, exc_type, exc_value, traceback):
        # Close the connection
        if self.conn:
            self.conn.close()
        # Propagate exceptions if any
        return False

# Usage of the custom context manager
query = "SELECT * FROM users WHERE age > ?"
params = (25,)

with ExecuteQuery("users.db", query, params) as results:
    print(results)
    