# coding=utf-8

import logging

import mongoengine

from utils import json_util

logger = logging.getLogger(__name__)


class APIJSONModelMixture(object):
    """API V1 Mixture 支持类，完成 JSON 格式化"""

    _api_fields = () # API 中显示的字段

    def to_api_dic(self):
        """convert object tot API JSON dic"""
        dic = {}
        fields = set(self._api_fields)
        for field in fields:
            try:
                attr = getattr(self, 'api_v1_' + field)
            except AttributeError:
                try:
                    attr = getattr(self, field)
                except AttributeError:
                    logger.error('Object %s has no field: %s' % (self, field))
                    raise Exception('Object %s has no field: %s' % (self, field))
            attr = json_util.format_value(attr)
            dic[field] = attr
        return dic


class Song(APIJSONModelMixture):
    _api_fields = ['title', 'singers', 'album_name', 'play_link', 'image']

    def __init__(self, title, singers, album_name, play_link, image, xiami_song_id):
        self.title = title
        self.singers = singers
        self.album_name = album_name
        self.play_link = play_link
        self.image = image
        self.xiami_song_id = xiami_song_id

    @staticmethod
    def from_xiami_song_info(song_info):
        song = Song(
            title=song_info['song_name'],
            singers=[song_info['singer']],
            image=song_info['album_logo'],
            play_link=song_info['listen_file'],
            album_name=song_info['album_name'],
            xiami_song_id=song_info['song_id'],
        )
        return song
