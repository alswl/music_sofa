# coding=utf-8

from top.api.rest.AlibabaXiamiApiSongDetailGetRequest import AlibabaXiamiApiSongDetailGetRequest
from top.api.rest.AlibabaXiamiApiSearchSongsGetRequest import AlibabaXiamiApiSearchSongsGetRequest
from top import appinfo as TopAppInfo

import settings


XIAMI_AUTH = TopAppInfo(settings.XIAMI_TOKEN, settings.XIAMI_SECRET)


def request_song_info(song_id):
    """
    {
        "listen_file": "http://m5.file.xiami.com/169/7169/585355777/1772360371_11138192_l.mp3?auth_key=27e57690177f9f2218e80e8747e4a847-1463270400-0-null",
        "mv_id": "",
        "album_id": 585355777,
        "demo": 0,
        "lyric_trc": "http://img.xiami.net/lyric/71/1772360371_1451896975_7163.trc",
        "play_seconds": 266,
        "play_authority": 1,
        "lyric": "http://img.xiami.net/lyric/71/1772360371_1453808132_1337.lrc",
        "is_check": 0,
        "rec_note": "",
        "logo": "http://img.xiami.net/images/album/img69/7169/5853557771385355777_1.jpg",
        "title": "麻油叶？不叫事儿！",
        "song_name": "安和桥",
        "encode_rate": 237,
        "music_type": 0,
        "favourite": false,
        "artist_id": 7169,
        "res_id": 11138192,
        "cd_serial": 1,
        "recommends": 57,
        "hash": "1be0f6bad766211d79e77e6f5539fc7a",
        "album_logo": "http://img.xiami.net/images/album/img69/7169/5853557771385355777_1.jpg",
        "track": 4,
        "default_resource_id": 11138192,
        "lyric_text": "让我再看你一遍 从南到北\r\n像是被五环路蒙住的双眼\r\n请你再讲一遍\r\n关于那天 抱着盒子的姑娘\r\n和擦汗的男人\r\n\r\n我知道\r\n那些夏天就像青春一样回不来\r\n代替梦想的\r\n也只能是勉为其难\r\n\r\n我知道\r\n吹过的牛逼也会随青春一笑了之\r\n让我困在城市里 纪念你\r\n\r\n让我再尝一口 秋天的酒\r\n一直往南方开 不会太久\r\n让我再听一遍\r\n最美的那一句 你回家了\r\n我在等你呢\r\n\r\n我知道\r\n那些夏天就像你一样回不来\r\n我已不会再对谁\r\n满怀期待\r\n\r\n我知道\r\n这个世界每天都有太多遗憾\r\n所以 你好 再见",
        "artist_name": "群星",
        "artist_logo": "http://img.xiami.net/images/artist/11952582166627_1.jpg",
        "singers": "宋冬野",
        "album_name": "麻油叶？不叫事儿！",
        "song_id": 1772360371,
        "name": "安和桥",
        "lyric_file": "http://img.xiami.net/lyric/71/1772360371_1453808132_1337.lrc",
        "flag": 0,
        "length": 266,
        "play_counts": 475590
    }
    """
    req = AlibabaXiamiApiSongDetailGetRequest()
    req.set_app_info(XIAMI_AUTH)
    req.id = song_id
    response = req.getResponse()
    song = response['user_get_response']['data']['song']

    return song


def search_song_info_by_name(key):
    """
    {
        "user_get_response": {
            "data": {
                "songs": {
                    "count": 21,
                    "data": [
                        {
                            "listen_file": "http://m5.file.xiami.com/169/7169/585355777/1772360371_11138192_l.mp3?auth_key=27e57690177f9f2218e80e8747e4a847-1463270400-0-null",
                            "is_play": 1,
                            "album_id": 585355777,
                            "demo": 0,
                            "lyric": "http://img.xiami.net/lyric/71/1772360371_1408420021_5505.lrc",
                            "album_sub_title": "",
                            "weight": 0,
                            "artist_sub_title": "Various Artists / 华语群星",
                            "song_name": "安和桥",
                            "sub_title": "",
                            "artist_id": 7169,
                            "cd_serial": 1,
                            "recommends": 57,
                            "album_logo": "http://img.xiami.net/images/album/img69/7169/5853557771385355777_1.jpg",
                            "track": 4,
                            "singer": "宋冬野",
                            "artist_name": "群星",
                            "flag": 0,
                            "lyric_karaok": "",
                            "album_name": "麻油叶？不叫事儿！",
                            "song_id": 1772360371,
                            "artist_logo": "http://img.xiami.net/images/artist/11952582166627_1.jpg",
                            "length": 266,
                            "play_counts": 0,
                            "doc_id": 0
                        }, {...}
                    ]
                }
            },
            "request_id": "46474901a5630314aa149c3599526d36"
        }
    }
    """
    req = AlibabaXiamiApiSearchSongsGetRequest()
    req.set_app_info(XIAMI_AUTH)
    req.key = key
    response = req.getResponse()
