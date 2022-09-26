import json
with open('WeaponData.json', 'r') as file:
    data = json.load(fp=file)
for weapon in data:
    if weapon['id'] == '2825865804':
        print(weapon)
print(None)
