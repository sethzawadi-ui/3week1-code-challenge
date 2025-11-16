# debug.py
# Debug runner for Magazine Domain Project - Commit 4

import sys
import os
sys.path.append(os.path.dirname(__file__))

from author import Author
from magazine import Magazine
from article import Article

if __name__ == "__main__":
    print("Magazine domain debug runner - Commit 4\n")

    # Authors
    author1 = Author("John Doe")
    author2 = Author("Jane Smith")
    author3 = Author("Mike Lee")

    # Magazines
    mag1 = Magazine("TechToday", "Technology")
    mag2 = Magazine("HealthNow", "Health")
    mag3 = Magazine("TravelFun", "Travel")

    # Articles
    Article(author1, mag1, "The Rise of AI")
    Article(author1, mag2, "Healthy Living Tips")
    Article(author1, mag1, "AI in 2025")        # John has 2 in TechToday now
    Article(author1, mag1, "Future of Robotics") # John has 3 in TechToday
    Article(author2, mag1, "Tech Innovations 2025")
    Article(author2, mag3, "Top Travel Spots")
    Article(author3, mag2, "Nutrition Myths")

    # ----------------------------------------
    # Test aggregate methods
    # ----------------------------------------
    print("Author1 topic areas:", author1.topic_areas())
    print("Mag1 article titles:", mag1.article_titles())
    print("Mag1 contributing authors (more than 2 articles):",
          [author.name for author in mag1.contributing_authors()] if mag1.contributing_authors() else None)
    print("Top publisher magazine:", Magazine.top_publisher().name)
