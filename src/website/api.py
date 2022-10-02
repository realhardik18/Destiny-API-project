from unicodedata import name
import discord_webhook
from creds import API_KEY_DESTINY, WEBHOOK_URL
import requests
import json
from discord_webhook import DiscordWebhook, DiscordEmbed
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
                                    'itemType': resp[id]['itemTypeDisplayName'],
                                    'flavorText': resp[id]['flavorText'],
                                    'damageType': resp[id]['defaultDamageType'],
                                    "icon": base_url + resp[id]['displayProperties']['icon'],
                                    "seen": False

                                }
                                dataToReturn.append(weaponData)
                    except Exception as e:
                        print(e)
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


def UpdateSeenStatus(id, status):
    with open('WeaponData.json', 'r') as file:
        data = json.load(file)
        for weapon in data:
            if weapon['id'] == str(id):
                weapon['seen'] = status
    with open('WeaponData.json', 'w') as file:
        json.dump(data, file)


def sendWebhook(info):
    webhook = DiscordWebhook(url=WEBHOOK_URL)
    embed = discord_webhook.DiscordEmbed(
        title=f"Weapon info for {info['name']}", description='note this is a preview')
    embed.add_embed_field(name='weapon id', value=str(info['id']))
    embed.add_embed_field(name='item type', value=str(info['itemType']))
    embed.add_embed_field(name='damage type', value=str(info['damageType']))
    embed.add_embed_field(name='flavor text', value=str(info['flavorText']))
    embed.set_thumbnail()
    webhook.add_embed(embed=embed)
    response = webhook.execute()


# print(GetAllValidWeaponsAsList())
# print(GetAllWeaponsData())
# print(GetAllWeaponsNames())
# print(GetAllWeaponsNamesFromJson())
# UpdateDataInJson()
# UpdateAllDataJson()
# print(GetJsonURL())
# UpdateDataInJson()
# print(GetJsonURL())
# UpdateDataInJson()
# print(GetAllValidWeapons())
# UpdateDataInJson()
