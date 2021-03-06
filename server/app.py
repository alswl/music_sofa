# coding=utf-8

from __future__ import unicode_literals, absolute_import

import sys
import os

import tornado.ioloop
import tornado.web
import tornado.template

import settings

sys.path.insert(0, 'libs')
reload(sys)
sys.setdefaultencoding('utf-8')


template_loader = tornado.template.Loader("templates")


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


def make_app():
    from handlers.web import RemoteHandler, ClientHandler
    from handlers.client_api import SongPlayHandler, SongSearchHandler
    from handlers.remote_api import RemoteWSHandler

    settings = {
        'debug': True,
        'autoreload': True,
    }

    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/remote", RemoteHandler),
        (r"/client", ClientHandler),
        (r"/ws/remote", RemoteWSHandler),
        (r"/api/song/play", SongPlayHandler),
        (r"/api/song/search", SongSearchHandler),
        (r"/static/(.*)", tornado.web.StaticFileHandler, {"path": "static"}),
    ], **settings)


if __name__ == "__main__":
    app = make_app()
    app.listen(port=settings.LISTEN_PORT, address=settings.LISTEN_ADDR)
    tornado.ioloop.IOLoop.current().start()
