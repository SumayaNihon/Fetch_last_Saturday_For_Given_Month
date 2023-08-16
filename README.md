# Fetch_Last_Saturday_For_Given_Month
# Last Saturday Finder

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







