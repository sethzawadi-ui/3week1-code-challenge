# author.py
# Author class implementation for Magazine Domain Project - Commit 3

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
        """Return all Article instances written by this author"""
        return self._articles

    def magazines(self):
        """Return unique Magazine instances this author has written for"""
        return list({article.magazine for article in self._articles})

    # ----------------------------------------
    # BONUS METHODS (placeholders)
    # ----------------------------------------
    def add_article(self, magazine, title):
        from article import Article  # avoid circular import
        article = Article(self, magazine, title)
        self._articles.append(article)
        magazine._articles.append(article)
        return article

    def topic_areas(self):
        if len(self._articles) == 0:
            return None
        return list({article.magazine.category for article in self._articles})
