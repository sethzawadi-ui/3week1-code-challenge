# author.py
# Author class implementation with aggregate methods

from typing import List
from article import Article
from magazine import Magazine

class Author:
    def __init__(self, name: str):
        if not isinstance(name, str):
            raise Exception("Author name must be a string.")
        if len(name.strip()) == 0:
            raise Exception("Author name cannot be empty.")

        self._name = name
        self._articles: List[Article] = []

    @property
    def name(self):
        return self._name

    # ----------------------------------------
    # RELATIONSHIP METHODS
    # ----------------------------------------
    def articles(self):
        return self._articles

    def magazines(self):
        return list({article.magazine for article in self._articles})

    # ----------------------------------------
    # AGGREGATE / BONUS METHODS
    # ----------------------------------------
    def add_article(self, magazine, title):
        """Creates a new Article associated with this author and the given magazine"""
        from article import Article  # avoid circular import
        article = Article(self, magazine, title)
        # Article constructor already registers with author and magazine
        return article

    def topic_areas(self):
        """Return unique list of categories of magazines this author has written for"""
        if len(self._articles) == 0:
            return None
        return list({article.magazine.category for article in self._articles})
