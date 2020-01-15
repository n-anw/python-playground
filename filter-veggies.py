# Nicholas and Rasim
import csv
import json
import pandas as pd 
from pprint import pprint

# Read vegetables.csv into a variable called vegetables.

with open('vegetables.csv', 'r') as f:
	vegetables = csv.DictReader(f)
	rows = list(vegetables)
	vegetables = [dict(row) for row in rows]


#pprint(vegetables)

# Loop through vegetables and filter down to only green 
# vegtables using a whitelist.

greenVeg = []
for veg in vegetables:
	if veg["color"] == "green":
		greenVeg.append(veg)

# Print veggies to the terminal
pprint(greenVeg)

# Write the veggies to a json file called greenveggies.json
with open('green-vegetables.json', 'w') as f:
    json.dump(greenVeg, f, indent = 4)

# Bonus: Output another csv called green_vegetables.csv.
with open('green_vegetables.csv', 'w') as f:
	writer = csv.writer(f)
	writer.writerow(['name', 'color'])
	for veg in greenVeg:
		writer.writerow([veg['name'], veg['color']])