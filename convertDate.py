# By Nicholas and Rasim

from datetime import datetime

# Set a variable birthday = "1-May-12".
birthday = "1-May-12"

# Parse the date using datetime.datetime.strptime.
parsed_date = datetime.strptime(birthday, "%d-%B-%y")

# Use strftime to output a date that looks like "5/1/2012".
date_output = parsed_date.strftime("%m/%-d/%Y")

print(date_output)