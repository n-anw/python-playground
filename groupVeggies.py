# Nicholas and Rasim
import csv
import json
from pprint import pprint

# Read vegtables.csv into a variable called vegtables.
with open('vegetables.csv', 'r') as f:
	vegetables = csv.DictReader(f)
	rows = list(vegetables)
	vegetables = [dict(row) for row in rows]

# Group vegtables by color as a variable vegetables_by_color.
vegetables_by_color = {}
for veg in vegetables:
	color = veg["color"]
	if color in vegetables_by_color:
		vegetables_by_color[color].append(veg)
	else: 
		vegetables_by_color[color] = [veg]

# pprint(vegetables_by_color)

# Output vegetables_by_color into a json called vegtables_by_color.json.
with open('vegetables_by_color.json', 'w') as f:
    json.dump(vegetables_by_color, f, indent = 4)