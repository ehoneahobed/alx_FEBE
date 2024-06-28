from datetime import datetime, timedelta

def display_current_datetime():
    # Get the current date and time
    current_date = datetime.now()
    # Format and print the current date and time
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

def calculate_future_date():
    # Prompt the user to enter a number of days
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    # Calculate the future date
    future_date = datetime.now() + timedelta(days=number_of_days)
    # Print the future date
    print("Future date:", future_date.strftime("%Y-%m-%d"))

def main():
    display_current_datetime()
    calculate_future_date()

if __name__ == "__main__":
    main()
