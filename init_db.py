from database import Base, engine
from models import User, Author, Book, Review, BookCategory, BookAuthor

def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()
