def convert_days(total_days):
    days_in_year = 365
    days_in_month = 30

    years = total_days // days_in_year
    remaining_days = total_days % days_in_year

    months = remaining_days // days_in_month
    days = remaining_days % days_in_month

    return years, months, days

day = int(input("Enter the day = "))
years,months,days = convert_days(day)
print(f"{years} Year, {months} months and {days} days ")

