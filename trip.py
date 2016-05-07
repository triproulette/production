import falcon
from DBHandler import DBHandler
from DBHandler import DBConnection


class Resource(object):

    def on_get(self, req, resp, trip_id, action, poi_id):

        if action == 'get_poi':
            conn = DBConnection.DBConnection()
            handler = DBHandler.DBHandler(conn)
            results = handler.query("SELECT p.title,p.description,p.category,e.s_time, e.e_time "+
                                    "FROM tr_db.poi as p JOIN tr_db.event as e ON e.poi_id = p.id")
            conn.close()

            print results[0][0], results[0][1]
            resp.body = '{msg: "bla"}'
            resp.status = falcon.HTTP_200
