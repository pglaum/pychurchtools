from __future__ import annotations

from tests import get_ct_client


class TestWiki:
    @classmethod
    def setup_class(cls):
        cls.ct = get_ct_client()

    def test_wiki(self):
        categories = self.ct.wiki.categories()
        assert categories
        pages = self.ct.wiki.pages(categories[0].id)
        assert pages
        assert self.ct.wiki.page(
            categories[0].id, pages[0].identifier, pages[0].version
        )
        assert self.ct.wiki.versions(categories[0].id, pages[0].identifier)

    def test_search(self):
        assert self.ct.wiki.search("Gott")
