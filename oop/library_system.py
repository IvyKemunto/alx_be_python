#!/usr/bin/env python3
"""
Task 1: Mastering Inheritance and Composition in Python
Library system demonstrating inheritance (Book -> EBook/PrintBook) and composition (Library)
"""

class Book:
    """Base class representing a general book"""
    
    def __init__(self, title, author):
        """
        Initialize a Book with title and author
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
        """
        self.title = title
        self.author = author
    
    def __str__(self):
        """String representation of a Book"""
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """Derived class representing an electronic book"""
    
    def __init__(self, title, author, file_size):
        """
        Initialize an EBook with title, author, and file size
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
            file_size (int): File size in KB
        """
        super().__init__(title, author)  # Call parent constructor
        self.file_size = file_size
    
    def __str__(self):
        """String representation of an EBook"""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """Derived class representing a physical printed book"""
    
    def __init__(self, title, author, page_count):
        """
        Initialize a PrintBook with title, author, and page count
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
            page_count (int): Number of pages in the book
        """
        super().__init__(title, author)  # Call parent constructor
        self.page_count = page_count
    
    def __str__(self):
        """String representation of a PrintBook"""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    """
    Composition class that manages a collection of books
    Demonstrates composition by containing Book objects
    """
    
    def __init__(self):
        """Initialize a Library with an empty collection of books"""
        self.books = []  # List to store book instances
    
    def add_book(self, book):
        """
        Add a book to the library collection
        
        Args:
            book: An instance of Book, EBook, or PrintBook
        """
        self.books.append(book)
    
    def list_books(self):
        """Print details of each book in the library"""
        for book in self.books:
            print(book)
