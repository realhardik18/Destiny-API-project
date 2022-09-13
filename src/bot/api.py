from creds import API_KEY_DESTINY
import requests

base_url = 'https://www.bungie.net/Platform'
header = {"x-api-key": API_KEY_DESTINY}


def GetJsonURL():
    resp = requests.get(url=base_url+'/Destiny2/Manifest/', headers=header)
    return 'https://www.bungie.net'+resp.json()['Response']['jsonWorldContentPaths']['en']


def GetAllValidWeapons():
    resp = requests.get(url=GetJsonURL(), headers=header)
    resp = resp.json()['DestinyInventoryItemDefinition']
    all_weapon_ids = resp.keys()
    #print('getting data..')
    dataToReturn = list()
    weaponsList = list()
    for id in all_weapon_ids:
        if resp[id]['inventory']['tierTypeHash'] == 4008398120:
            if 1 in resp[id]['itemCategoryHashes']:
                try:
                    if resp[id]['quality']['versions'][0]['powerCapHash'] == 2759499571:
                        if resp[id]['displayProperties']['name'] not in weaponsList:
                            weaponsList.append(
                                resp[id]['displayProperties']['name'])
                            weaponData = {
                                'name': resp[id]['displayProperties']['name'],
                                'id': id
                            }
                            dataToReturn.append(weaponData)
                except Exception as e:
                    pass
    return dataToReturn


print(len(GetAllValidWeapons()))
# print(GetAllValidWeapons())
