import mysql.connector


class DBHandler(object):
    db_connection = None

    def __init__(self, db_connection):
        self.db_connection = db_connection

    def __print__(self):
        print("User: " + self.db_connection.user)
        print("Password: " + self.db_connection.password)
        print("Host: " + self.db_connection.host)
        print("DB: " + self.db_connection.database)

    def query(self, query):
        m = self.db_connection.connection.cursor()
        m.execute(query)
        return m.fetchall()

    def execute(self, query):
        m = self.db_connection.connection.cursor()
        m.execute(query)
        self.db_connection.commit()
        return m.lastrowid

    def create(self, table_name, table_fields, table_values):
        q = "INSERT INTO {} ({}) VALUES({})".format(table_name, table_fields, table_values)
        print q
        return self.execute(q)







