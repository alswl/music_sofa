# coding=utf-8

import unittest2

from models import music


class ITMusic(unittest2.TestCase):

    def test_split(self):
        song_info = music.request_song_info(1772360371)
        self.assertTrue('file.xiami.com' in song_info['listen_file'])

