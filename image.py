
import os
import uuid
import mimetypes

import falcon

class Resource(object):

      def on_get(self, req, resp, name):
        try:
            resp.content_type = mimetypes.guess_type(name)[0]
            image_path = os.path.join(self.storage_path, name)
            resp.stream = open('pics\triprollete.jpg', 'rb')
            resp.stream_len = os.path.getsize('pics\triprollete.jpg')
        except Exception as e:
            resp.body = '{"message": %s}' % e.message
            resp.status = falcon.HTTP_200


