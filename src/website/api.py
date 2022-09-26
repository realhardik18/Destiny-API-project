from creds import API_KEY_DESTINY
import requests
import json

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
            if 'iconWatermark' in resp[id].keys():
                if 1 in resp[id]['itemCategoryHashes']:
                    try:
                        if resp[id]['quality']['versions'][0]['powerCapHash'] == 2759499571:
                            if resp[id]['displayProperties']['name'] not in weaponsList:
                                weaponsList.append(
                                    resp[id]['displayProperties']['name'])
                                weaponData = {
                                    "name": resp[id]['displayProperties']['name'].replace(' ', '-'),
                                    "id": id,
                                    'item-type': resp[id]['itemTypeDisplayName'],
                                    'flavor-text': resp[id]['flavorText'],
                                    'damage-type': resp[id]['defaultDamageType']

                                }
                                dataToReturn.append(weaponData)
                    except Exception as e:
                        pass
    return dataToReturn


def GetAllValidWeaponsAsList():
    resp = GetAllValidWeapons()
    weapons = list()
    for item in resp:
        weapons.append(item['name'].replace(' ', '-'))
    return weapons


def UpdateDataInJson():
    with open('WeaponData.json', 'w') as f:
        json.dump(GetAllValidWeapons(), f)


def GetAllWeaponsDataFromJson():
    with open('WeaponData.json', 'r') as f:
        data = json.load(f)
    return data


def GetAllWeaponsNamesFromJson():
    names = ''
    for item in GetAllWeaponsDataFromJson():
        names += item['name'].replace(' ', '-')+' '
    return names


def UpdateAllDataJson():
    resp = requests.get(url=GetJsonURL(), headers=header)
    resp = resp.json()['DestinyInventoryItemDefinition']
    with open('AllData.json', "w+") as file:
        json.dump(resp, file)


def GetWeaponFromJson(id):
    with open('WeaponData.json', 'r') as file:
        data = json.load(file)
        for weapon in data:
            if weapon['id'] == str(id):
                return weapon
# print(GetAllValidWeaponsAsList())
# print(GetAllWeaponsData())
# print(GetAllWeaponsNames())
# print(GetAllWeaponsNamesFromJson())
# UpdateDataInJson()
# UpdateAllDataJson()
# print(GetJsonURL())
