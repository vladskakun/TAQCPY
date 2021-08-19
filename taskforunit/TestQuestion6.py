"""
Date Format
Create a function that converts a date formatted as MM/DD/YYYY to YYYYDDMM.
Examples
format_date("11/12/2019") ➞ "20191211"

format_date("12/31/2019") ➞ "20193112"

format_date("01/15/2019") ➞ "20191501"
Notes
Return value should be a string.

"""


import datetime


def format_date(data):
    data = datetime.datetime.strptime(data, "%m/%d/%Y").strftime("%Y%m%d")
    return data


print(format_date("11/12/2019"))