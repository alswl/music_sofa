# coding=utf-8

from tornado.websocket import WebSocketHandler

import play


class RemoteWSHandler(WebSocketHandler):

    def open(self):
        play.remote_join(self)
        print("WebSocket opened")

    def on_message(self, message):
        self.write_message(u"You said: " + message)

    def on_close(self):
        print("WebSocket closed")
