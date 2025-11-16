# lib/author.py
# Author class placeholder for the Magazine domain project.

class Author:
    """
    Placeholder Author class.
    We'll implement behavior in later commits.
    """
    def __init__(self, name):
        # store raw name for now; validations will come later
        self._name = name

    @property
    def name(self):
        # simple accessor
        return self._name
