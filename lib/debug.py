# debug.py
# Debug runner for Magazine Domain Project - Commit 1
# Run this file to test that your initial classes are importable and working.

from author import Author
from magazine import Magazine
from article import Article

if __name__ == "__main__":
    print("Magazine domain debug runner - Commit 1\n")

    # Create sample Author
    author1 = Author("John Doe")
    print("Author created:", author1.name)

    # Create sample Magazine
    mag1 = Magazine("TechToday", "Technology")
    print("Magazine created:", mag1.name, "-", mag1.category)

    # Create sample Article
    article1 = Article(author1, mag1, "The Rise of AI")
    print("Article created with title:", article1.title)
    print("Article's author:", article1.author.name)
    print("Article's magazine:", article1.magazine.name)

    # Test relationships (placeholders, will work after adding relationship methods)
    try:
        print("Author articles:", author1.articles())
    except AttributeError:
        print("Author articles method not implemented yet.")

    try:
        print("Magazine articles:", mag1.articles())
    except AttributeError:
        print("Magazine articles method not implemented yet.")

    print("\nDebug complete. Ready for next commit.")
