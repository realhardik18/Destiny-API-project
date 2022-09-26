import os
import json


data = list()
for item in os.listdir('GIFS'):
    data.append(''.join(item.split(' ')[:-1]).lower().replace(' ', ''))


with open('data.json', 'r') as file:
    data = json.load(file)
for item in data:
    print(item['name'].lower().replace('-', '') in data)
