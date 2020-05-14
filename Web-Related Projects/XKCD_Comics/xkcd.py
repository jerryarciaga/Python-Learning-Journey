#!/usr/bin/python

import requests, bs4
import os

# Create folder for XKCD
if not os.access('XKCD', os.F_OK):
    os.mkdir('XKCD')
os.chdir('XKCD')

xkcd_site = 'https://xkcd.com/'
xkcd_request = requests.get(xkcd_site)
while xkcd_request.status_code == 200:
    xkcd_soup = bs4.BeautifulSoup(xkcd_request.text, 'html.parser')
    title = xkcd_soup.select('#ctitle')
    print(f'Downloading {title[0].text}')
    # TODO Perform download
    prev_link = xkcd_site + xkcd_soup.select(f'''#middleContainer > 
        ul:nth-child(2) > li:nth-child(2) > a
        ''')[0].get('href')
    xkcd_request = requests.get(prev_link)
