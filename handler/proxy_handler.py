import tornado.httpclient
from tornado.httputil import url_concat

import base_handler
from conf import remote_host

import ssl
ssl.match_hostname = lambda cert, hostname: True

class proxy_handler(base_handler.BaseHandler):

    def get(self, path):
        self.http_execute(path, 'GET')

    def post(self, path):
        self.http_execute(path, 'POST')

    def put(self, path):
        self.http_execute(path, 'PUT')

    def delete(self, path):
        self.http_execute(path, 'DELETE')

    def http_execute(self, path, method):
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
        # headers['Cookie'] = 'lang=zh-cn; udb_version=1.0; udb_uid=1199511680931; udb_passport=35184372292947hy; yyuid=1199511680931; udb_biztoken=AQBqb7FWTVsW2jLjMIMBx3ikWEwW3DWAa7EWuexPpDuamWQmRwAm0HLiVuDHN1QQVkpdb0Zv48JebJtIjTIPYrtvA5gRmQFYTedVGP4wZYTSrc2iFXNP7LsrioZdjyVK6XtB8BThydlaKtKQxJ8O4msx1N59iZvsgJ1VMHbrDwo6E7JVLWf304IKuQ-3iGKaHLrgQozax7e3ziTuK5VKKHwNVBwgc17fP6BbpGkTFi8-B87NwinfekyiSbjZ_Rj-5O0W8UY6seYukQlWDrbAYS4pOoODkLXuxU2d6Syr_qzukiRjP3DnGAuTGq2Zxku9-p6tvOTujdAaunL45TVWSnSu; udb_origin=1; build=1; nick=Yaoguo#6191; avatar=http://image.msstatic.com/cdnimage/avatar/1019/82/20d8b3e7f2ed9af4b76a5141c0123320d8b3e7f2ed9af4b76a5141c01233_1517541907.jpg; admin_uid=1; admin_email=admin%40yy.com'

        body = self.request.body
        if method == 'GET' or method == 'DELETE':
            body = None

        http_client = tornado.httpclient.HTTPClient()
        try:
            response = http_client.fetch(real_url, headers=headers, method=method, body=body)
            self.write(response.body)
        except tornado.httpclient.HTTPError as e:
            # print "Error:", e
            # self.write({'code': '500'})
            raise e
        finally:
            http_client.close()