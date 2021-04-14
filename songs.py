"""
Songs
=====

Endpoints for Songs

"""

from ct_types import Song


class CTSongs:

    def __init__(self, CT):

        self.CT = CT

    def songs(self):

        # TODO: query parameters

        res = self.CT.make_request('songs')

        songs = []
        if res and 'data' in res:
            for item in res['data']:
                songs.append(Song(item))

        return songs

    def song(self, song_id):

        route = f'songs/{song_id}'
        res = self.CT.make_request(route)

        if res and 'data' in res:
            return Song(res['data'])

        return None

    def songs_of_event(self, event_id):

        route = f'events/{event_id}/agenda/songs'
        res = self.CT.make_request(route)

        songs = []
        if res and 'data' in res:
            for item in res['data']:
                songs.append(Song(item))

        return songs
