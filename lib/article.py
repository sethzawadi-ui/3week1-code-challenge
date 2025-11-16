# lib/article.py
# Article class placeholder for the Magazine domain project.

class Article:
    """
    Placeholder Article class.
    We'll add logic and global Article._all in later commits.
    """
    def __init__(self, author, magazine, title):
        self._author = author
        self._magazine = magazine
        self._title = title

    @property
    def title(self):
        return self._title
