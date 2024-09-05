"""
Wiki
====

Endpoints for the wiki.

"""

from __future__ import annotations

from typing import Any

from .models.wiki import WikiCategory, WikiPage, WikiSearchResult


class Wiki:
    def __init__(self, ct: Any) -> None:
        """Initialize a Status object."""

        self.__ct = ct

    def categories(self) -> list[WikiCategory]:
        """Get all wiki categories.

        :returns: List of wiki categories
        :rtype: List[WikiCategory]
        """

        res = self.__ct.make_request("wiki/categories")

        ctgs = []
        if res and "data" in res:
            for item in res["data"]:
                ctg = WikiCategory(**item)
                ctgs.append(ctg)

        return ctgs

    def pages(self, category_id: int) -> list[WikiPage]:
        """Get all pages in a wiki category.

        :param category_id: The ID of the category
        :type category_id: int
        :returns: All pages in the category
        :rtype: List[WikiPage]
        """

        res = self.__ct.make_request(f"wiki/categories/{category_id}/pages")

        pgs = []
        if res and "data" in res:
            for item in res["data"]:
                pg = WikiPage(**item)
                pgs.append(pg)

        return pgs

    def page(
        self, category_id: int, identifier: str, version: int | None = None
    ) -> WikiPage | None:
        """Get a wiki page.

        :param category_id: The ID of the category
        :type category_id: int
        :param identifier: The ID of the page
        :type identifier: int
        :param version: The revision of the page
        :type version: int
        :returns: The wiki page
        :rtype: WikiPage
        """

        if version:
            res = self.__ct.make_request(
                f"wiki/categories/{category_id}/"
                f"pages/{identifier}/"
                f"versions/{version}"
            )
        else:
            res = self.__ct.make_request(
                f"wiki/categories/{category_id}/" f"pages/{identifier}"
            )

        if res and "data" in res:
            return WikiPage(**res["data"])

        return None

    def versions(self, category_id: int, identifier: str) -> list[WikiPage]:
        """Get the versions of a wiki page.

        :param category_id: The ID of the category
        :type category_id: int
        :param identifier: The ID of the page
        :type identifier: int
        :returns: The wiki page
        :rtype: WikiPage
        """

        res = self.__ct.make_request(
            f"wiki/categories/{category_id}/" f"pages/{identifier}/versions"
        )

        pgs = []
        if res and "data" in res:
            for item in res["data"]:
                pgs.append(WikiPage(**item))

        return pgs

    def search(
        self, query: str, wiki_category_ids: list[int] | None = None
    ) -> list[WikiSearchResult]:
        """Search for a query.

        :param query: The search query
        :type query: str
        :param wiki_category_ids: Search only in these categories. Search in
            all categories, if this is None
        :returns: The search results
        :rtype: List[WikiSearchResult]
        """

        params: dict[str, Any] = {}

        params["query"] = query
        if wiki_category_ids:
            params["wiki_category_ids"] = wiki_category_ids

        res = self.__ct.make_request("wiki/search", params)

        results = []
        if res and "data" in res:
            for item in res["data"]:
                result = WikiSearchResult(**item)
                results.append(result)

        return results
