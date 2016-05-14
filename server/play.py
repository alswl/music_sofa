# coding=utf-8

from tornado import websocket

from utils import json_util

rooms_handlers = {
    'default': []
}

last_song = {
}


def remote_join(handler, room='default'):
    if room not in rooms_handlers:
        rooms_handlers[room] = []
    rooms_handlers[room].append(handler)


def send_play_command(song, handler, room='default'):
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


def play_song(song, room='default'):
    for handler in rooms_handlers.get(room, []):
        send_play_command(room=room, song=song, handler=handler)

    last_song[room] = song
    return len(rooms_handlers.get(room, []))


def get_online_count(room='default'):
    return len(rooms_handlers.get(room, []))


def heartbeat(room='default'):
    for handler in rooms_handlers.get(room, []):
        try:
            handler.write_message('ping')
        except websocket.WebSocketClosedError:
            rooms_handlers[room].remove(handler)
    return len(rooms_handlers.get(room, []))


def get_last_song(room='default'):
    return last_song.get(room, '')
