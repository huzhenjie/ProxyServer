# -*- encoding: utf-8 -*-
import os

import tornado.httpserver
import tornado.web
from tornado.options import define, options

import conf
from handler import proxy_handler

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            ("/", IndexHandler),
            (r"/(.*)", proxy_handler.proxy_handler),
        ]
        settings = dict(
            # blog_title = u"Tornado Blog",
            # template_path = os.path.join(os.path.dirname(__file__), "templates"),
            # static_path = os.path.join(os.path.dirname(__file__), "static"),
            # ui_modules = {"Entry": EntryModule},
            # xsrf_cookies = True,
            # cookie_secret = "__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
            # login_url = "/tmp/ts_recommend_server.log",
            debug=True,
        )
        if conf.static_file_dir and conf.static_file_dir != '' and os.path.exists(conf.static_file_dir) and os.path.isdir(conf.static_file_dir):
            settings['static_path'] = conf.static_file_dir
        else:
            print 'static path [' + conf.static_file_dir + '] not exist'
        super(Application, self).__init__(handlers, **settings)

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('<h2>Welcome to <a href="https://github.com/huzhenjie/ProxyServer">ProxyServer</a></h2>')

def main():
    print 'To see your app, visit:\n\nhttp://localhost:%s' % options.port
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    define("port", default=conf.port, help="run on the given port", type=int)
    main()
