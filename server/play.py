# coding=utf-8

from tornado import websocket

from utils import json_util

rooms_handlers = {
    'default': []
}


def remote_join(handler, room='default'):
    if room not in rooms_handlers:
        rooms_handlers[room] = []
    rooms_handlers[room].append(handler)


def play_song(song, room='default'):
    for handler in rooms_handlers.get(room, []):
        command = {
            'action': 'play',
            'params': {
                'song': song
            }
        }
        try:
            handler.write_message(json_util.format_value(command))
        except websocket.WebSocketClosedError:
            rooms_handlers[room].remove(handler)
    return len(rooms_handlers.get(room, []))


def get_online_count(room='default'):
    return len(rooms_handlers.get(room, []))
