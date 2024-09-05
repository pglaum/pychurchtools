"""
Songs
=====

Endpoints for Songs

"""

from __future__ import annotations

from typing import Any

from .models.pagination import MetaPagination
from .models.song import Song


class Songs:
    def __init__(self, ct: Any) -> None:
        self.__ct = ct

    def get_all(
        self,
        song_category_ids: list[int] | None = None,
        ids: list[int] | None = None,
        practice: bool = False,
        key_of_arrangement: str | None = None,
        page: int = 1,
        limit: int = 10,
    ) -> tuple[list[Song], MetaPagination | None]:
        """Return a list of songs.

        :param song_category_ids: Only query for these category IDs
        :type song_category_ids: List[int]
        :param ids: Only query for these IDs
        :type ids: List[int]
        :param practice: Query for songs that "should be practiced"
        :type practice: bool
        :param key_of_arrangement: Query for keys of an arrangement of the song
        :type key_of_arrangement: str
        :param page: Result page number
        :type page: int
        :param limit: Result item count
        :type limit: int
        :returns: A list of songs that match the query
        :rtype: List[Song]
        """

        params: dict[str, Any] = {}

        if song_category_ids:
            params["song_category_ids"] = song_category_ids
        if ids:
            params["ids"] = ids
        if practice:
            params["practice"] = practice
        if key_of_arrangement:
            params["key_of_arrangement"] = key_of_arrangement
        if page:
            params["page"] = page
        if limit:
            params["limit"] = limit

        res = self.__ct.make_request("songs", params=params)

        songs = []
        if res and "data" in res:
            for item in res["data"]:
                song = Song(**item)
                songs.append(song)

        pagination = None
        if res and "meta" in res:
            pagination = MetaPagination(**res["meta"])

        return songs, pagination

    def get(self, song_id: int) -> Song | None:
        """Get a song by id.

        :param song_id: The ID of the song
        :type song_id: int
        :returns: The song
        :rtype: Song
        """

        route = f"songs/{song_id}"
        res = self.__ct.make_request(route)

        if res and "data" in res:
            return Song(**res["data"])

        return None
