# Nick Anway

# import packages

import json
import csv

# read json file to superheroes variable

with open('superheroes.json', 'r') as f:
	superheroes = json.load(f)

# write the header row into a new csv file

with open('superheroes.csv', 'w') as f:
	writer = csv.writer(f)
	headers = ["name", "age", "secretIdentity", "powers", "squadName", "homeTown", "formed", "secretBase", "active"]
	writer.writerow(headers)

# iterate over members

	members = superheroes['members']
	for member in members:
		powers = member["powers"]

# iterate over powers

		for power in powers:
			powerSingle = power 
			name = member["name"]
			age = member["age"]
			secretIdentity = member["secretIdentity"]
			powers = member["powers"]
			squadName = superheroes["squadName"]
			homeTown = superheroes["homeTown"]
			formed = superheroes["formed"]
			secretBase = superheroes["secretBase"]
			active = superheroes["active"]

# write one row for each power

			row = [name, age, secretIdentity, powerSingle, squadName, homeTown, formed, secretBase, active]
			writer.writerow(row)