"""Question 1:

Create a table named books containing the following fields:

id: A serial number that serves as the Primary Key with Auto Increment.
title: The title of the book, which must be unique.
price: The price of the book, which must be a decimal value and cannot be NULL.
Tasks:
Insert the following books into the table:

Title: "Harry Potter and the Sorcerer's Stone" | Price: 89.90
Title: "The Little Prince" | Price: 45.50
Title: "1984" | Price: 79.90
Title: "Les Misérables" | Price: 99.00
Title: "Crime and Punishment" | Price: 69.90
Write a query that retrieves and prints all books from the table.

Write a query that retrieves and prints only the books with a price greater than 70.

Write a query that updates the price of the book "1984" to 89.5.

Write a query that deletes the books whose price is 99.
========================================================================"""

from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker, declarative_base

# Database connection
engine = create_engine("sqlite:///books.db", echo=True)
Base = declarative_base()

# Define the Book model
class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, unique=True, nullable=False)
    price = Column(Float, nullable=False)

# Create the books table
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Insert books
def insert_books():
    books = [
        Book(title="Harry Potter and the Sorcerer's Stone", price=89.90),
        Book(title="The Little Prince", price=45.50),
        Book(title="1984", price=79.90),
        Book(title="Les Misérables", price=99.00),
        Book(title="Crime and Punishment", price=69.90),
    ]
    session.add_all(books)
    session.commit()

# Retrieve and print all books
def get_all_books():
    books = session.query(Book).all()
    for book in books:
        print(f"ID: {book.id}, Title: {book.title}, Price: {book.price}")

# Retrieve and print books with price > 70
def get_expensive_books():
    books = session.query(Book).filter(Book.price > 70).all()
    for book in books:
        print(f"Title: {book.title}, Price: {book.price}")

# Update the price of '1984' to 89.5
def update_book_price():
    book = session.query(Book).filter(Book.title == "1984").first()
    if book:
        book.price = 89.5
        session.commit()

# Delete books with price = 99
def delete_expensive_books():
    session.query(Book).filter(Book.price == 99).delete()
    session.commit()

# Run functions
insert_books()
get_all_books()
print("\nBooks with price > 70:")
get_expensive_books()
update_book_price()
delete_expensive_books()
print("\nAfter updates:")
get_all_books()
