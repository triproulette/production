import mysql.connector
from Entities.POI import POI
from Entities.GeoLocation import GeoLocation


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
        self.db_connection.connection.commit()
        return m.lastrowid

    def create(self, table_name, table_fields, table_values):
        q = "INSERT INTO {} ({}) VALUES({})".format(table_name, table_fields, table_values)
        print q
        return self.execute(q)

    def getPoi(self, poi_id):
        res = self.query("SELEC * FROM poi WHERE id = '{}'".format(poi_id))
        if len(res) <= 0:
            return None
        else:
            row = res[0]
            poi = POI()
            poi._title = row["title"]
            poi._description = row["description"]
            poi._activityTime = row["activity_time"]
            poi._category = row["category"]
            poi._image = row["image"]
            geo_loc = (row["geoLocation"]).split(",")
            poi._geoLocation = GeoLocation(latitude=geo_loc[0],longitude=geo_loc[1])
            poi._grade = row["grade"]
            return poi








