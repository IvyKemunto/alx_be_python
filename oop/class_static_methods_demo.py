#!/usr/bin/env python3
"""
Task 3: Distinguishing Between Class Methods and Static Methods
Calculator class demonstrating the difference between @classmethod and @staticmethod
"""


class Calculator:
    """Calculator class demonstrating class methods and static methods"""
    
    # Class attribute
    calculation_type = "Arithmetic Operations"
    
    @staticmethod
    def add(a, b):
        """
        Static method to add two numbers
        
        Args:
            a (float): First number
            b (float): Second number
            
        Returns:
            float: Sum of a and b
            
        Note:
            Static methods don't have access to class or instance attributes
        """
        return a + b
    
    @classmethod
    def multiply(cls, a, b):
        """
        Class method to multiply two numbers
        
        Args:
            cls: Reference to the class itself
            a (float): First number
            b (float): Second number
            
        Returns:
            float: Product of a and b
            
        Note:
            Class methods have access to class attributes through 'cls' parameter
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
