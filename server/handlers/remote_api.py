# coding=utf-8

from tornado.websocket import WebSocketHandler, WebSocketClosedError

import play
from utils import json_util


class RemoteWSHandler(WebSocketHandler):

    def open(self):
        play.remote_join(self)
        song = play.get_last_song()
        play.send_play_command(song, self)
        print("WebSocket opened")

    def on_message(self, message):
        self.write_message(u"You said: " + message)

    def on_close(self):
        print("WebSocket closed")
