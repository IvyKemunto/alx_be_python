#!/usr/bin/env python3
"""
Task 2: Exploring Polymorphism and Method Overriding
Shape hierarchy demonstrating polymorphism through method overriding
"""

import math


class Shape:
    """Base class for geometric shapes"""
    
    def area(self):
        """
        Calculate the area of the shape
        This method should be overridden by derived classes
        
        Raises:
            NotImplementedError: Indicates that derived classes must override this method
        """
        raise NotImplementedError("Derived classes must override the area() method")


class Rectangle(Shape):
    """Rectangle class that inherits from Shape"""
    
    def __init__(self, length, width):
        """
        Initialize a Rectangle with length and width
        
        Args:
            length (float): The length of the rectangle
            width (float): The width of the rectangle
        """
        self.length = length
        self.width = width
    
    def area(self):
        """
        Calculate the area of the rectangle
        
        Returns:
            float: Area of the rectangle (length × width)
        """
        return self.length * self.width


class Circle(Shape):
    """Circle class that inherits from Shape"""
    
    def __init__(self, radius):
        """
        Initialize a Circle with radius
        
        Args:
            radius (float): The radius of the circle
        """
        self.radius = radius
    
    def area(self):
        """
        Calculate the area of the circle
        
        Returns:
            float: Area of the circle (π × radius²)
        """
        return math.pi * self.radius ** 2
