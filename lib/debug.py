# debug.py
# Debug runner for Magazine Domain Project - Commit 3

import sys
import os
sys.path.append(os.path.dirname(__file__))

from author import Author
from magazine import Magazine
from article import Article

if __name__ == "__main__":
    print("Magazine domain debug runner - Commit 3\n")

    # Authors
    author1 = Author("John Doe")
    author2 = Author("Jane Smith")

    # Magazines
    mag1 = Magazine("TechToday", "Technology")
    mag2 = Magazine("HealthNow", "Health")

    # Articles
    article1 = Article(author1, mag1, "The Rise of AI")
    article2 = Article(author1, mag2, "Healthy Living Tips")
    article3 = Article(author2, mag1, "Tech Innovations 2025")

    # ----------------------------------------
    # Test Author relationship methods
    # ----------------------------------------
    print("Author1 articles:", author1.articles())
    print("Author1 magazines:", author1.magazines())

    print("Author2 articles:", author2.articles())
    print("Author2 magazines:", author2.magazines())

    # ----------------------------------------
    # Test Magazine relationship methods
    # ----------------------------------------
    print("Mag1 articles:", mag1.articles())
    print("Mag1 contributors:", [author.name for author in mag1.contributors()])

    print("Mag2 articles:", mag2.articles())
    print("Mag2 contributors:", [author.name for author in mag2.contributors()])
