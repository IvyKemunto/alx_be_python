from datetime import datetime, timedelta

def display_current_datetime():
    """
    Display the current date and time in a readable format (YYYY-MM-DD HH:MM:SS).
    """
    # Get the current date and time
    current_date = datetime.now()
    
    # Format and print the current date and time
    formatted_datetime = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_datetime}")
    
    return current_date

def calculate_future_date(days_to_add):
    """
    Calculate and return a future date by adding specified number of days to current date.
    
    Args:
        days_to_add (int): Number of days to add to the current date
    
    Returns:
        datetime: Future date
    """
    # Get current date
    current_date = datetime.now()
    
    # Calculate future date by adding the specified number of days
    future_date = current_date + timedelta(days=days_to_add)
    
    # Format and print the future date
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future_date}")
    
    return future_date

def main():
    """
    Main function to demonstrate datetime operations.
    """
    print("=== Exploring Python's datetime Module ===\n")
    
    # Part 1: Display current date and time
    current_datetime = display_current_datetime()
    
    # Part 2: Calculate future date
    try:
        # Prompt user for number of days
        days_input = input("Enter the number of days to add to the current date: ")
        days_to_add = int(days_input)
        
        # Calculate and display future date
        future_datetime = calculate_future_date(days_to_add)
        
        # Additional information (optional)
        print(f"\nAdditional Information:")
        print(f"Days added: {days_to_add}")
        print(f"Current day of week: {current_datetime.strftime('%A')}")
        print(f"Future day of week: {future_datetime.strftime('%A')}")
        
    except ValueError:
        print("Error: Please enter a valid integer for the number of days.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
