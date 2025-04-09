import json

people_string = '''
{
  "people": [
    {
      "name": "John Smith",
      "phone": "615-555-7164",
      "emails": ["johnsmit@bogusemail.com", "john.smith@work-place.com"],
      "has_license": false
    },
    {
      "name": "Jane Doe",
      "phone": "560-555-5153",
      "emails": null,
      "has_license": true
    }   
    ]
}
'''

# [loads] - Load the json string into a python object
data = json.loads(people_string)
print(type(data))           # This will be a dict
print(data)
print(type(data['people']), end='\n\n') # This will be a list

# Loop through the list
for person in data['people']:
  print(person)
  print(person['name'])
print()

# [dumps] - Dump a Python object into a json string (reverse of above)
# Remove the phone number value
for person in data['people']:
  del person['phone']
# Dump object into a new json string
new_string = json.dumps(data)
print(new_string, end='\n\n')

# Indent the json
new_string_indent = json.dumps(data, indent=2) # This will format the indent of 2 for each level
print(new_string_indent, end='\n\n')

# Sort the keys
sort_keys = json.dumps(data, indent=2, sort_keys=True) # Sorts the keys alphabetically
print(sort_keys, end='\n\n')

# -- Load a file -- #

# Open and load with load method
with open('states.json', 'r') as f:
  data = json.load(f)  # This will load the json file as a Python object

for state in data['states']:
  print(state)
  print(state['name'], state['abbreviation']) # Access the items in the json

# Write the Python object out to a json file
# Remove the area codes
for state in data['states']:
  del state['area_codes']

# Write using the dump method
with open('new_states.json', 'w') as f:
  json.dump(data, f, indent=2) # Dump (data) into the file (f)