# Since 1958, Canadian Thanksgiving has occurred on the second Monday in
# October. Write a function that takes a year (>1957) as a parameter, and
# returns the number of days between Canadian Thanksgiving and Christmas.

import calendar


def shopping_days(year):
    """year an int > 1957
       returns the number of days between Canadian Thanksgiving and
            Christmas in year"""
    month = calendar.monthcalendar(year, 10)
    if month[0][calendar.MONDAY] != 0:
        thanksgiving = month[1][calendar.MONDAY]
    else:
        thanksgiving = month[2][calendar.MONDAY]
    return (25 + 30 + 31 - thanksgiving)
