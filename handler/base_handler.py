# -*- encoding: utf-8 -*-
import tornado.web

class BaseHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS, DELETE, PUT')

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
