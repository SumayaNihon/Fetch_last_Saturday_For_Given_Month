# Fetch_Last_Saturday_For_Given_Month
# Last&Total Saturday Finder

This Python script helps you find the last Saturday of a specified month and year. It also counts the total number of Saturdays in that month.

## Table of Contents

- [Description](#description)
- [Usage](#usage)
- [Functionality](#functionality)
- [How to Run](#how-to-run)
- [Example](#example)

## Description

This script provides a function called `last_saturday_finder(year, month)` that determines the last Saturday of the given month and year. It also counts and displays the total number of Saturdays in that month.

## Usage

The primary purpose of this script is to help you find the last Saturday of a specific month and year, and to count the total number of Saturdays in that month.

## Functionality

- The script calculates and displays the last Saturday of the provided month and year.
- It counts and displays the total number of Saturdays in the same month.

## How to Run

1. Make sure you have Python installed on your system.
2. Download or clone the script to your local machine.
3. Open a terminal or command prompt and navigate to the script's directory.
4. Run the script using the command: `python3 Last_Saturday_Finder.py`


## Code Explanation

This Python script uses the datetime module to find the last Saturday of a given month and calculate the total number of Saturdays in that month. It defines a function last_saturday(year, month) which takes the year and month as inputs and performs the following tasks:

1. Calculates the last day of the given month using datetime.date(year, month + 1, 1) - datetime.timedelta(days=1).

2. Determines the offset required to find the last Saturday by calculating (last_day.weekday() - 5) % 7.

3. Calculates the date of the last Saturday by subtracting the offset from the last day of the month.

4. Prints the last Saturday's day along with the appropriate ordinal indicator (e.g., "1st," "2nd," "3rd," "4th," "5th," etc.).

5. Initializes counters for the total number of Saturdays and starts iterating through the days of the month using a loop.

6. For each day, checks if the weekday index is 5 (indicating Saturday) and increments the total_saturdays counter.

7. Prints the calculated total number of Saturdays for the given month.
## Example

```python

import datetime

def last_saturday_finder(year,month):
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

last_saturday_finder(2023,6)







