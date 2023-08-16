import datetime

def last_saturday(year,month):
    last_day = datetime.date(year, month + 1, 1) - datetime.timedelta(days=1)
    offset = (last_day.weekday() - 5) % 7
    saturday = last_day - datetime.timedelta(days=offset)
    print(f"Last Saturday: {saturday.day}th")

    total_saturdays = 0
    first_day = datetime.date(year, month, 1)
    current_day = first_day
    
    while current_day.month == month:
        if current_day.weekday() == 5:  
            total_saturdays += 1
        current_day += datetime.timedelta(days=1)
    
    print(f"Total Saturdays: {total_saturdays}")

last_saturday(2023,6)