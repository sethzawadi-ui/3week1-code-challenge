# debug.py
# Debug runner for Magazine Domain Project
# Tests all features including relationships and aggregate methods

import sys
import os
sys.path.append(os.path.dirname(__file__))

from author import Author
from magazine import Magazine
from article import Article

if __name__ == "__main__":
    print("Magazine domain debug runner - Full Version\n")

    # ------------------------------
    # Create Authors
    # ------------------------------
    author1 = Author("John Doe")
    author2 = Author("Jane Smith")
    author3 = Author("Mike Lee")

    # ------------------------------
    # Create Magazines
    # ------------------------------
    mag1 = Magazine("TechToday", "Technology")
    mag2 = Magazine("HealthNow", "Health")
    mag3 = Magazine("TravelFun", "Travel")

    # ------------------------------
    # Create Articles
    # ------------------------------
    Article(author1, mag1, "The Rise of AI")
    Article(author1, mag2, "Healthy Living Tips")
    Article(author1, mag1, "AI in 2025")
    Article(author1, mag1, "Future of Robotics")
    Article(author2, mag1, "Tech Innovations 2025")
    Article(author2, mag3, "Top Travel Spots")
    Article(author3, mag2, "Nutrition Myths")

    # ------------------------------
    # Test Author Methods
    # ------------------------------
    print("Author1 articles:", author1.articles())
    print("Author1 magazines:", [mag.name for mag in author1.magazines()])
    print("Author1 topic areas:", author1.topic_areas())

    # ------------------------------
    # Test Magazine Methods
    # ------------------------------
    print("Mag1 article titles:", mag1.article_titles())
    contributing = mag1.contributing_authors()
    print("Mag1 contributing authors (more than 2 articles):",
          [a.name for a in contributing] if contributing else None)
    print("Top publisher magazine:", Magazine.top_publisher().name)
