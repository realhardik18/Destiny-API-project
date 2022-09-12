from logging import exception
import requests
from msedge.selenium_tools import EdgeOptions
from msedge.selenium_tools import Edge
import time
from bs4 import BeautifulSoup as bs4
import requests


edge_options = EdgeOptions()
edge_options.use_chromium = True
# edge_options.add_argument('headless')
# edge_options.add_argument('disable-gpu')
# edge_options.add_argument('log-level=3')
driver = Edge(executable_path='edgedriver_win64\msedgedriver.exe',
              options=edge_options)
# driver.get('https://example.com')

# TODO
# WRITE SCRIPT TO MAKE A DATABASE OF ALL WEAPONS ALONG WITH THEIR IDS AND SAVE
# IN A CSV OR JSON FILE, SCRAPE THIS https://destinytracker.com/destiny-2/db/items/weapon

# THEN WORK ON AUTOCOMEPLETEWITH DISCORD BOT
