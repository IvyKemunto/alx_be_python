#!/usr/bin/env python3
"""
Task 0: Dive into Python Magic Methods
A Book class that demonstrates constructors, destructors, and representation methods
"""

class Book:
    """A class representing a book with magic methods implementation"""
    
    def __init__(self, title, author, year):
        """
        Constructor: Initialize a Book instance
        
        Args:
            title (str): The title of the book
            author (str): The author of the book  
            year (int): The publication year of the book
        """
        self.title = title
        self.author = author
        self.year = year
    
    def __del__(self):
        """
        Destructor: Called when object is garbage collected
        Prints a message indicating the book is being deleted
        """
        print(f"Deleting {self.title}")
    
    def __str__(self):
        """
        String Representation: Informal string representation for end users
        
        Returns:
            str: Human-readable string representation of the book
        """
        return f"{self.title} by {self.author}, published in {self.year}"
    
    def __repr__(self):
        """
        Official Representation: Technical string representation for developers
        
        Returns:
            str: String that would recreate the Book instance
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"
