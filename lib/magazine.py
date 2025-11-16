# magazine.py
# Magazine class implementation with aggregate methods

from typing import List
from author import Author
from article import Article

class Magazine:
    _all_magazines = []  # For top_publisher()

    def __init__(self, name: str, category: str):
        # Validate name
        if not isinstance(name, str):
            raise Exception("Magazine name must be a string.")
        if not (2 <= len(name) <= 16):
            raise Exception("Magazine name must be 2–16 characters.")

        # Validate category
        if not isinstance(category, str):
            raise Exception("Category must be a string.")
        if len(category.strip()) == 0:
            raise Exception("Category cannot be empty.")

        self._name = name
        self._category = category
        self._articles: List[Article] = []

        # Register this magazine in the class-level list
        Magazine._all_magazines.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception("Magazine name must be a string.")
        if not (2 <= len(value) <= 16):
            raise Exception("Magazine name must be 2–16 characters.")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise Exception("Category must be a string.")
        if len(value.strip()) == 0:
            raise Exception("Category cannot be empty.")
        self._category = value

    # ----------------------------------------
    # RELATIONSHIP METHODS
    # ----------------------------------------
    def articles(self):
        return self._articles

    def contributors(self):
        return list({article.author for article in self._articles})

    # ----------------------------------------
    # AGGREGATE / BONUS METHODS
    # ----------------------------------------
    def article_titles(self):
        """Return list of all article titles for this magazine"""
        if len(self._articles) == 0:
            return None
        return [article.title for article in self._articles]

    def contributing_authors(self):
        """Return list of authors with more than 2 articles in this magazine"""
        from collections import Counter
        if len(self._articles) == 0:
            return None
        counter = Counter([article.author for article in self._articles])
        result = [author for author, count in counter.items() if count > 2]
        if len(result) == 0:
            return None
        return result

    @classmethod
    def top_publisher(cls):
        """Return the magazine with the most articles"""
        if len(cls._all_magazines) == 0:
            return None
        return max(cls._all_magazines, key=lambda mag: len(mag.articles()))
