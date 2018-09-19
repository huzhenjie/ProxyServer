# -*- encoding: utf-8 -*-
import tornado.web

class BaseHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        headers = self.request.headers
        if 'origin' in headers and headers['origin'] and headers['origin'] != '':
            self.set_header("Access-Control-Allow-Origin", headers['origin'])
        else:
            self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "X-Requested-With,Content-Type,Content-Length,Authorization")
        self.set_header("Access-Control-Allow-Credentials", "true")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS, DELETE, PUT')

    def options(self, *args, **kwargs):
        self.set_status(204)
        self.finish()

    # @property
    # def db(self):
    #     return self.application.db
    #
    # @staticmethod
    # def success(data=None):
    #     if data is None:
    #         return {'code': 200, 'msg': 'ok'}
    #     return {'code': 200, 'msg': 'ok', 'data': data}
    #
    # @staticmethod
    # def not_found(msg=None):
    #     if msg is None:
    #         return {'code': 404, 'msg': '没有找到相关数据'}
    #     return {'code': 404, 'msg': msg}
    #
    # @staticmethod
    # def empty_list():
    #     return {'code': 200, 'msg': 'ok', 'data': []}
