import mysql.connector

class DBHandler:
    db_connection = None

    def __init__(self, db_connection):
        self.db_connection = db_connection

    def __print__(self):
        print("User: " + self.db_connection.user)
        print("Password: " + self.db_connection.password)
        print("Host: " + self.db_connection.host)
        print("DB: " + self.db_connection.database)


    def execute_query(self, query):
        m = self.db_connection.connection.cursor()
        m.execute(query)
        return m.fetchall()
#

    def create_user(self):

    def read_user(self):

    def update_user(self):

    def delete_user(self):








