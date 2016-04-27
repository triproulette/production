
import os
import uuid
import mimetypes

import falcon

class Resource(object):

      def on_get(self, req, resp):
        try:
            resp.content_type = mimetypes.guess_type('a')[0]
            image_path = os.path.join('pics\\', 'a')
            resp.stream = open('triprollete.jpg', 'rb')
            resp.stream_len = os.path.getsize('triprollete.jpg')
        except Exception as e:
            resp.body = '{"error": %s}' % e.message
            resp.status = falcon.HTTP_200


