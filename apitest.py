from creds import API_KEY_DESTINY
import requests

base_url = 'https://www.bungie.net/Platform'
header = {"x-api-key": API_KEY_DESTINY}
#resp = requests.get(url=base_url+'/Destiny2/Manifest/', headers=header)
# print(resp.json()['Response']['jsonWorldContentPaths']['en'])
resp = requests.get(
    url='https://www.bungie.net/common/destiny2_content/json/en/aggregate-94816ad1-160a-492e-94df-db5bf726bee3.json', headers=header)
resp = resp.json()['DestinyInventoryItemDefinition']
all_weapon_ids = resp.keys()
print('getting data..')
uniqueLegendaryWeapons = set()
for id in all_weapon_ids:
    if resp[id]['inventory']['tierTypeHash'] == 4008398120:
        if 'iconWatermark' in resp[id].keys():
            if 1 in resp[id]['itemCategoryHashes']:
                uniqueLegendaryWeapons.add(
                    resp[id]['displayProperties']['name'])
for weapon in uniqueLegendaryWeapons:
    print(weapon)
print(f'number of weapons in this category->{len(uniqueLegendaryWeapons)}')
