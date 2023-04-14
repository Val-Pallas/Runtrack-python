import json
import os

data = {
    'employees': [
        {
            'name': 'John Doe',
            'department': 'Marketing',
            'place': 'Remote'
        },
        {
            'name': 'tio',
            'department': 'Software Engineering',
            'place': 'Remote'
        },
        {
            'name': 'tio',
            'department': 'Software Engineering',
            'place': 'Office'
        },
        {
            'name': 'Tia',
            'department': 'Software Engineering',
            'place': 'Office'
        }
    ]
}

# .dumps() as a string
json_string = json.dumps(data)
print(json_string)

# Using a JSON file
with open('json_data.json', 'w') as outfile:
    outfile.write(json_string)

if os.path.isfile('json_data.json'):
    with open('json_data.json') as json_file:
        loaded_data = json.load(json_file)
        print(loaded_data)
else:
    print('json_data.json not found in current directory.')
