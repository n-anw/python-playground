# Nicholas Anway

# example 1
import csv
import json
from pprint import pprint

with open('testwrite.csv', 'w') as f:
	writer = csv.writer(f)
	writer.writerow(['col1', 'col2'])
	count = 3
	while count > 0:
		writer.writerow(['row1', 'row2'])
		count -= 1


# example 2
with open('vegetables.csv', 'r') as f:
	reader = csv.DictReader(f)
	rows = list(reader)
	roes = [dict(row) for row in rows]

pprint(rows)

# example 3: writing a json file
rows = [
    {"name": "Rachel", "age": 34},
    {"name": "Monica", "age": 34},
    {"name": "Phoebe", "age": 37}
]

with open('testwrite.json', 'w') as f:
    json.dump(rows, f)

# example 3: reading a json file
with open('friends.json', 'r') as f:
	data = json.load(f)

pprint(data)
