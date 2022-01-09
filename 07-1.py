# Write a function that meets the specification

import calendar


def shopping_days(year):
    """year an int >= 1941
       returns the number of days between U.S. Thanksgiving and
            Christmas in year"""
    month = calendar.monthcalendar(year, 11)
    if month[0][calendar.THURSDAY] != 0:
        thanksgiving = month[3][calendar.THURSDAY]
    else:
        thanksgiving = month[4][calendar.THURSDAY]
    return (55 - thanksgiving)
