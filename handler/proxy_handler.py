import tornado.httpclient
from tornado.httputil import url_concat

import base_handler
from conf import remote_host


class proxy_handler(base_handler.BaseHandler):

    def get(self, path):
        arguments = self.request.arguments
        params = {}
        for k, v in arguments.items():
            # print k, v
            params[k] = v[0]
        if path and path.startswith('/'):
            path = path[1:]
        real_url = '%s/%s' % (remote_host, path)
        real_url = url_concat(real_url, params)
        print real_url
        headers = self.request.headers
        # print headers
        http_client = tornado.httpclient.HTTPClient()
        try:
            response = http_client.fetch(real_url, headers=headers)
            self.write(response.body)
        except tornado.httpclient.HTTPError as e:
            print "Error:", e
            self.write({'code': '500'})
        finally:
            http_client.close()

    def post(self, path):
        arguments = self.request.arguments
        params = {}
        for k, v in arguments.items():
            # print k, v
            params[k] = v[0]
        if path and path.startswith('/'):
            path = path[1:]
        real_url = '%s/%s' % (remote_host, path)
        real_url = url_concat(real_url, params)
        print real_url
        headers = self.request.headers
        body = self.request.body
        # print headers
        http_client = tornado.httpclient.HTTPClient()
        try:
            response = http_client.fetch(real_url, headers=headers, body=body, method='POST')
            self.write(response.body)
        except tornado.httpclient.HTTPError as e:
            print "Error:", e
            self.write({'code': '500'})
        finally:
            http_client.close()