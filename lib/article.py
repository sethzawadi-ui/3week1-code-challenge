# article.py
# Article class implementation for Magazine Domain Project - Commit 2

from author import Author
from magazine import Magazine

class Article:
    # Class-level list to store all articles
    _all = []

    def __init__(self, author, magazine, title):
        # Validate author
        if not isinstance(author, Author):
            raise Exception("author must be an Author instance.")
        # Validate magazine
        if not isinstance(magazine, Magazine):
            raise Exception("magazine must be a Magazine instance.")
        # Validate title
        if not isinstance(title, str):
            raise Exception("title must be a string.")
        if not (5 <= len(title) <= 50):
            raise Exception("title must be between 5 and 50 characters.")

        # Set private attributes
        self._author = author
        self._magazine = magazine
        self._title = title

        # Add this article to the class-level list
        Article._all.append(self)

        # Register this article with author and magazine
        author._articles.append(self)
        magazine._articles.append(self)

    # ----------------------------------------
    # PROPERTIES
    # ----------------------------------------
    @property
    def title(self):
        """Title is immutable after creation"""
        return self._title

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception("New author must be an Author instance.")
        self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise Exception("New magazine must be a Magazine instance.")
        self._magazine = value

    # ----------------------------------------
    # REPRESENTATION
    # ----------------------------------------
    def __repr__(self):
        return f"<Article '{self._title}'>"
