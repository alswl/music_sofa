# coding=utf-8

import unittest2

from api import xiami_api


class ITXiami(unittest2.TestCase):

    def test_request_song_info(self):
        song_info = xiami_api.request_song_info(1772360371)
        self.assertTrue('file.xiami.com' in song_info['listen_file'])

    def test_search_song_by_name(self):
        song_info = xiami_api.search_song_info_by_name('安河桥')

