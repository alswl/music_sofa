# coding=utf-8

from __future__ import unicode_literals

import sys

import tornado.ioloop
import tornado.web


sys.path.insert(0, 'libs')


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
