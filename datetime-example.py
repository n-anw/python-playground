# Nicholas Anway
# Reference http://strftime.org/ for the format string codes

from datetime import datetime

raw_date = "2017-01-11"
date_format = "%Y-%m-%d"

# take the string object type and read into python datetime format
parsed_date = datetime.strptime(raw_date, date_format)

# or...
parsed_date = datetime.strptime(raw_date, "%Y-%m-%d")

# convert parsed date to a string in a given format
date_str = parsed_date.strftime("%m/%d/%y")

print(raw_date)
print(parsed_date)
print(date_str)
