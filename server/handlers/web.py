# coding=utf-8

import json

from tornado.web import RequestHandler

from app import template_loader
import settings
import play


class RemoteHandler(RequestHandler):

    def get(self):
        self.write(template_loader.load("remote.html").generate(
            listen_addr=settings.LISTEN_ADDR, listen_port=settings.LISTEN_PORT,
            online_count=play.get_online_count()
        ))


class ClientHandler(RequestHandler):

    def get(self):
        self.write(template_loader.load("client.html").generate(
            listen_addr=settings.LISTEN_ADDR, listen_port=settings.LISTEN_PORT,
            online_count=play.get_online_count()
        ))
