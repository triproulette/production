import falcon
import json
from DBHandler import DBHandler
from DBHandler import DBConnection


class Resource(object):

    def on_get(self, req, resp, trip_id, action, event_id):

        if action == 'get_event':
            ev_count = 5    # 4 events each request

            conn = DBConnection.DBConnection()
            handler = DBHandler.DBHandler(conn)
            #   get next ev_count events
            results = handler.query("SELECT e.id,p.title,p.description,p.category,e.s_time, e.e_time "+
                                    "FROM tr_db.poi as p JOIN tr_db.event as e ON e.poi_id = p.id "+
                                    "ORDER BY e.id ASC LIMIT {},{}".format(event_id,ev_count))
            #   conn.close()
            """
            print results

            json_event = ()
            for i in range(ev_count):
                try:
                    ev = '{{ trip_id: {}, title: {}, desc: {}, category: {}, start_time: {}, end_time: {} }}'\
                        .format(results[i])
                    print ev
                    json_event.append(ev)
                except:
                    print 'error appending'
                    print '{}'.format(len(results[i]))
                    print '{}'.format(results[i])
                    continue

            resp.body = '{{ events: [ {} ] }}'.format(', '.join(json_event))
            """

            json_string = json.dumps(results)
            resp.body = '{{ {} }}'.format(results)
            resp.status = falcon.HTTP_200
