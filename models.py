from sqlalchemy import Column, Integer, String, ForeignKey, Table, Boolean
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

class Author(Base):
    __tablename__ = 'author'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    surname = Column(String)
    year = Column(Integer)
    books = relationship('Book', secondary='book_author', back_populates='authors')

class BookAuthor(Base):
    __tablename__ = 'book_author'
    author_id = Column(Integer, ForeignKey('author.id'), primary_key=True)
    book_id = Column(Integer, ForeignKey('book.id'), primary_key=True)

class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    ISBN = Column(String)
    price = Column(Integer)
    image = Column(String)
    year = Column(Integer)
    book_category_id = Column(Integer, ForeignKey('books_category.id'))
    reviews = relationship('Review', back_populates='book')
    authors = relationship('Author', secondary='book_author', back_populates='books')

class Review(Base):
    __tablename__ = 'review'
    id = Column(Integer, primary_key=True, index=True)
    comment = Column(String)
    star_given = Column(Integer)
    user_id = Column(Integer, ForeignKey('user.id'))
    book_id = Column(Integer, ForeignKey('book.id'))
    book = relationship('Book', back_populates='reviews')
    user = relationship('User')

class BookCategory(Base):
    __tablename__ = 'books_category'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    books = relationship('Book', back_populates='category')
