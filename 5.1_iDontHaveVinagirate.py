import random
import datetime

def generate_random_date(start_date, end_date):
    # Calculate the total number of days between the two dates
    days_diff = (end_date - start_date).days

    # Generate a random number of days between 0 and the total number of days
    random_days = random.randint(0, days_diff)

    # Add the random number of days to the start date to get the new date
    new_date = start_date + datetime.timedelta(days=random_days)

    return new_date


def get_start_date():
    while True:
        try:
            start_date_str = input("Enter the start date in the format YYYY-MM-DD: ")
            start_date = datetime.datetime.strptime(start_date_str, "%Y-%m-%d")
            return start_date
        except ValueError:
            print("Invalid date format. Please enter a valid date.")


def get_end_date():
    while True:
        try:
            end_date_str = input("Enter the end date in the format YYYY-MM-DD: ")
            end_date = datetime.datetime.strptime(end_date_str, "%Y-%m-%d")
            return end_date
        except ValueError:
            print("Invalid date format. Please enter a valid date.")


def main():
    start_date = get_start_date()
    end_date = get_end_date()

    # Generate a random date between the two input dates
    new_date = generate_random_date(start_date, end_date)

    # Check if the new date falls on a Monday
    if new_date.weekday() == 0:
        print("The new date falls on a Monday.")
    else:
        print("The new date does not fall on a Monday.")

    print("Random date:", new_date.strftime("%Y-%m-%d"))


if __name__ == '__main__':
    main()

