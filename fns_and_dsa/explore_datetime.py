from datetime import datetime, timedelta

def display_current_datetime():
    """
    Display the current date and time in a readable format (YYYY-MM-DD HH:MM:SS).
    """
    # Get the current date and time and save in current_date variable
    current_date = datetime.now()
    
    # Format and print the current date and time
    formatted_datetime = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_datetime}")

def calculate_future_date():
    """
    Calculate and display a future date by adding specified number of days to current date.
    """
    # Get current date
    current_date = datetime.now()
    
    # Prompt user for number of days
    days_input = input("Enter the number of days to add to the current date: ")
    days_to_add = int(days_input)
    
    # Calculate future date by adding the specified number of days and save in future_date variable
    future_date = current_date + timedelta(days=days_to_add)
    
    # Format and print the future date
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future_date}")

def main():
    """
    Main function to demonstrate datetime operations.
    """
    # Part 1: Display current date and time
    display_current_datetime()
    
    # Part 2: Calculate future date
    calculate_future_date()

if __name__ == "__main__":
    main()
