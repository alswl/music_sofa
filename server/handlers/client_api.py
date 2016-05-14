# coding=utf-8

import json

from tornado.web import RequestHandler

from api import xiami_api
from models import Song


class SongPlayHandler(RequestHandler):

    def put(self):
        self.write("Hello, world")


class SongSearchHandler(RequestHandler):

    def post(self):
        keyword = self.get_argument('keyword')
        song_infos = xiami_api.search_song_info_by_name(keyword)
        songs = [Song.from_xiami_song_info(x) for x in song_infos]
        self.add_header('X-count', len(songs))
        self.write(json.dumps([x.to_api_dic() for x in songs]))

