"""
Songs
=====

Endpoints for Songs

"""

from ct_types import Song
from typing import List


class Songs:

    def __init__(self, CT):

        self.CT = CT

    def list(self, song_category_ids: List[int] = None, ids: List[int] = None,
             practice: bool = False, key_of_arrangement: str = None,
             page: int = 1, limit: int = 10) -> List[Song]:

        # TODO: pagination

        params = {}

        if song_category_ids:
            params['song_category_ids'] = song_category_ids
        if ids:
            params['ids'] = ids
        if practice:
            params['practice'] = practice
        if key_of_arrangement:
            params['key_of_arrangement'] = key_of_arrangement
        if page:
            params['page'] = page
        if limit:
            params['limit'] = limit

        res = self.CT.make_request('songs', params=params)

        songs = []
        if res and 'data' in res:
            for item in res['data']:
                song = Song(**item)
                songs.append(song)

        return songs

    def get(self, song_id):

        route = f'songs/{song_id}'
        res = self.CT.make_request(route)

        if res and 'data' in res:
            return Song(**res['data'])

        return None
