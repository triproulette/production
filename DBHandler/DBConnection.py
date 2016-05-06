import mysql.connector
import time


class DBConnection(object):
    instance = None
    connection = None

    def __new__(cls):
        if DBConnection.instance is None:
            DBConnection.instance = object.__new__(cls)
        return DBConnection.instance

    def __init__(self, user='trip', password='trip', host='10.10.20.209', database='tr_db'):
        self.user = user
        self.password = password
        self.host = host
        self.database = database
        if DBConnection.connection is None:
            DBConnection.connection = mysql.connector.connect(user=user, password=password, host=host, database=database)
            print('Database connection opened.')


    def __del__(self):
        if DBConnection.connection is not None:
            DBConnection.close()
            print('Database connection closed.')

    def close(self):
        self.connection.close()
