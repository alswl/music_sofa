# coding=utf-8

import json

from tornado.web import RequestHandler

from api import xiami_api
from models import Song
import play


class SongPlayHandler(RequestHandler):

    def put(self):
        """
        """
        xiami_song_id = self.get_argument('song_id')
        song_info = xiami_api.request_song_info(xiami_song_id)
        if song_info is None:
            self.set_status(404)
            return
        song = Song.from_xiami_song_info(song_info)
        count = play.play_song(song)
        self.write(json.dumps({'count': count}))


class SongSearchHandler(RequestHandler):

    def get(self):
        """
        http -f POST http://127.0.0.1:8888/api/song/search keyword=J
        """
        keyword = self.get_argument('keyword')
        song_infos = xiami_api.search_song_info_by_name(keyword)
        songs = [Song.from_xiami_song_info(x) for x in song_infos]
        self.add_header('X-count', len(songs))
        self.write(json.dumps([x.to_api_dic() for x in songs]))

