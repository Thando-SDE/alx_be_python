from datetime import datetime, timedelta

def display_current_datetime():

    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    return current_date

def calculate_future_date(days):

    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    return formatted_future_date

current_date = display_current_datetime()

try:
    days = int(input("Enter the number of days to add to the current date: "))
    future_date = calculate_future_date(days)
    print(f"Future date: {future_date}")
except ValueError:
    print("Please enter a valid integer number of days.")