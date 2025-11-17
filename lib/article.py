# article.py
# Article class with validation and relationships
# Circular import resolved using local imports

class Article:
    _all = []

    def __init__(self, author, magazine, title):
        # Local imports to avoid circular import
        from author import Author
        from magazine import Magazine

        # Validate inputs
        if not isinstance(author, Author):
            raise Exception("author must be an Author instance.")
        if not isinstance(magazine, Magazine):
            raise Exception("magazine must be a Magazine instance.")
        if not isinstance(title, str):
            raise Exception("title must be a string.")
        if not (5 <= len(title) <= 50):
            raise Exception("title must be between 5 and 50 characters.")

        self._author = author
        self._magazine = magazine
        self._title = title

        # Add to class-level list and to author/magazine
        Article._all.append(self)
        author._articles.append(self)
        magazine._articles.append(self)

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        from author import Author
        if not isinstance(value, Author):
            raise Exception("New author must be an Author instance.")
        self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        from magazine import Magazine
        if not isinstance(value, Magazine):
            raise Exception("New magazine must be a Magazine instance.")
        self._magazine = value

    def __repr__(self):
        return f"<Article '{self._title}'>"
