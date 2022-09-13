import pandas as pd


def GetAllWeapons():
    data = pd.read_csv('weaponAndIDS.csv', error_bad_lines=False)
    return list(set(data['name'].to_list()))


# print(returnCommands())
