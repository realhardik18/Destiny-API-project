from msedge.selenium_tools import EdgeOptions
from msedge.selenium_tools import Edge
import requests

edge_options = EdgeOptions()
edge_options.use_chromium = True
edge_options.add_argument('headless')
edge_options.add_argument('disable-gpu')
edge_options.add_argument('log-level=3')

driver = Edge(executable_path='edgedriver_win64\msedgedriver.exe',
              options=edge_options)

with open('weaponAndIds.csv', "w") as file:
    file.write('sno,name,id\n')

sno = 1

for page in range(1, 23):
    driver.get(
        f'https://destinytracker.com/destiny-2/db/items/weapon?page={page}')
    items = driver.find_elements_by_class_name('item__name')
    for item in items:
        IDpart = item.get_attribute('href').replace(
            'https://destinytracker.com/destiny-2/db/items/', '')
        weaponID = IDpart[:IDpart.index('-')]
        weaponName = item.text
        with open('weaponAndIDS.csv', 'a+') as file:
            file.write(f'{sno},{weaponName},{weaponID}\n')
        print(f'we at {sno}')
        sno += 1

# TODO
# WRITE SCRIPT TO MAKE A DATABASE OF ALL WEAPONS ALONG WITH THEIR IDS AND SAVE
# IN A CSV OR JSON FILE, SCRAPE THIS https://destinytracker.com/destiny-2/db/items/weapon
# 22 PAGES OF DATA
# THEN WORK ON AUTOCOMEPLETEWITH DISCORD BOT
