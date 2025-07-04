def safe_divide(numerator, denominator):
    """
    Safely divide two numbers with robust error handling.
    
    Args:
        numerator: The numerator (can be string or number)
        denominator: The denominator (can be string or number)
    
    Returns:
        str: Result message or error message
    """
    try:
        # Try to convert inputs to floats
        num = float(numerator)
        denom = float(denominator)
        
        # Try to perform division
        result = num / denom
        return f"The result of the division is {result}"
        
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."
