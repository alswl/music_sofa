# coding=utf-8


from top.api.rest.AlibabaXiamiApiSongDetailGetRequest import AlibabaXiamiApiSongDetailGetRequest
from top.api.rest.AlibabaXiamiApiSearchSongsGetRequest import AlibabaXiamiApiSearchSongsGetRequest
from top import appinfo as TopAppInfo

import settings


XIAMI_AUTH = TopAppInfo(settings.XIAMI_TOKEN, settings.XIAMI_SECRET)


def request_song_info(song_id):
    """
{u'album_id': 44,
 u'album_logo': u'http://img.xiami.net/images/album/img18/18/44_1.jpg',
 u'album_name': u'\u5929\u4f7f\u7684\u7fc5\u8180',
 u'artist_id': 18,
 u'artist_logo': u'http://img.xiami.net/images/artistlogo/63/14112733865563_1.jpg',
 u'artist_name': u'\u5b89\u7425',
 u'cd_serial': 1,
 u'default_resource_id': 15316,
 u'demo': 0,
 u'favourite': False,
 u'hash': u'8eacf6b755970cdf695e59bf5c394003',
 u'is_check': 0,
 u'length': 220,
 u'listen_file': u'http://m5.file.xiami.com/18/18/44/376568_15316_l.mp3?auth_key=d3622372d5d6dc29ecc66dbc6680e807-1411603200-0-null',
 u'logo': u'http://img.xiami.net/images/album/img18/18/44_1.jpg',
 u'lyric': u'http://img.xiami.net/lyric/upload/68/376568_1326015214.lrc',
 u'lyric_file': u'http://img.xiami.net/lyric/upload/68/376568_1326015214.lrc',
 u'lyric_text': u'\u843d\u53f6\u968f\u98ce\u5c06\u8981\u53bb\u4f55\u65b9\r\n\u53ea\u7559\u7ed9\u5929\u7a7a\u7f8e\u4e3d\u4e00\u573a\r\n\u66fe\u98de\u821e\u7684\u8eab\u5f71\r\n\u50cf\u5929\u4f7f\u7684\u7fc5\u8180\r\n\u5212\u8fc7\u6211\u5e78\u798f\u7684\u8fc7\u5f80\r\n\r\n\u7231\u66fe\u7ecf\u6765\u5230\u8fc7\u7684\u5730\u65b9\r\n\u4f9d\u7a00\u7559\u7740\u6628\u5929\u7684\u82ac\u82b3\r\n\u90a3\u719f\u6089\u7684\u6e29\u6696\r\n\u50cf\u5929\u4f7f\u7684\u7fc5\u8180\r\n\u5212\u8fc7\u6211\u65e0\u8fb9\u7684\u5fc3\u4f24\r\n\r\n\u76f8\u4fe1\u4f60\u8fd8\u5728\u8fd9\u91cc\r\n\u4ece\u4e0d\u66fe\u79bb\u53bb\r\n\u6211\u7684\u7231\u50cf\u5929\u4f7f\u5b88\u62a4\u4f60\r\n\r\n\u82e5\u751f\u547d\u53ea\u5230\u8fd9\u91cc\r\n\u4ece\u6b64\u6ca1\u6709\u6211\r\n\u6211\u4f1a\u627e\u4e2a\u5929\u4f7f\u66ff\u6211\u53bb\u7231\u4f60\r\n\r\nDrum Programmer: \u8c2d\u660e\u8f89\r\nBass: \u8c2d\u660e\u8f89\r\nGuitar: \u6c5f\u5efa\u6c11\r\n\u5408\u58f0\uff1a\u5f20\u6c5f\u3001\u7aa6\u9896\r\n\r\nOP: Typhoon Music (HK) Limited\r\nSP: \u4e0a\u6d77\u6b65\u5347\u5927\u98ce\u97f3\u4e50\u6587\u5316\u4f20\u64ad\u6709\u9650\u516c\u53f8',
 u'lyric_trc': u'',
 u'mv_id': u'',
 u'name': u'\u5929\u4f7f\u7684\u7fc5\u8180',
 u'play_authority': 1,
 u'play_counts': 1079240,
 u'play_seconds': 220,
 u'rec_note': u'',
 u'recommends': 2314,
 u'res_id': 15316,
 u'singers': u'\u5b89\u7425',
 u'song_id': 376568,
 u'song_name': u'\u5929\u4f7f\u7684\u7fc5\u8180',
 u'title': u'\u5929\u4f7f\u7684\u7fc5\u8180',
 u'track': 3}
"""
    req = AlibabaXiamiApiSongDetailGetRequest()
    req.set_app_info(XIAMI_AUTH)
    req.id = song_id
    response = req.getResponse()
    song = response['user_get_response']['data']['song']

    return song


def search_song_by_name(key):
    req = AlibabaXiamiApiSearchSongsGetRequest()
    req.set_app_info(XIAMI_AUTH)
    req.key = key
    response = req.getResponse()
    __import__('ipdb').set_trace()
