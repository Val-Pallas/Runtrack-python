import json

with open('job02_my_passwords.json') as f:
    data = json.load(f)
    previous_passwords = []
    for i in data:
        current_password = data[i]['my_password']
        if current_password in previous_passwords:
            print(current_password, previous_passwords,'object repeated')
            break
        else:
            previous_passwords.append(current_password)
    else:
        print( 'no duplicates found')

