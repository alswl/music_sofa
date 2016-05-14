# coding=utf-8

import json

from tornado.web import RequestHandler

from app import template_loader


class RemoteHandler(RequestHandler):

    def get(self):
        self.write(template_loader.load("remote.html").generate(myvalue="XXX"))


class ClientHandler(RequestHandler):

    def get(self):
        self.write("Hello, world")
