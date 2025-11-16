# debug.py
# Debug runner for Magazine Domain Project - Commit 2

import sys
import os
sys.path.append(os.path.dirname(__file__))

from author import Author
from magazine import Magazine
from article import Article

if __name__ == "__main__":
    print("Magazine domain debug runner - Commit 2\n")

    # Create sample Author
    author1 = Author("John Doe")
    author2 = Author("Jane Smith")
    print("Authors created:", author1.name, "and", author2.name)

    # Create sample Magazine
    mag1 = Magazine("TechToday", "Technology")
    mag2 = Magazine("HealthNow", "Health")
    print("Magazines created:", mag1.name, "-", mag1.category, "and", mag2.name, "-", mag2.category)

    # Create sample Articles
    article1 = Article(author1, mag1, "The Rise of AI")
    article2 = Article(author1, mag2, "Healthy Living Tips")
    article3 = Article(author2, mag1, "Tech Innovations 2025")
    print("\nArticles created:")
    print(article1)
    print(article2)
    print(article3)

    # Check Article._all
    print("\nAll articles in Article._all:", Article._all)

    # Test mutability
    print("\nChanging author of article2 to Jane Smith...")
    article2.author = author2
    print("article2 new author:", article2.author.name)

    print("Changing magazine of article3 to HealthNow...")
    article3.magazine = mag2
    print("article3 new magazine:", article3.magazine.name)

    # Titles remain immutable
    print("article1 title:", article1.title)
