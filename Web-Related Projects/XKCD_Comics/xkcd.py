#!/usr/bin/python

import requests, bs4
import os

## Create folder for XKCD
#if not os.access('XKCD', os.F_OK):
#    os.mkdir('XKCD')
#os.chdir('XKCD')

xkcd_request = requests.get('https://xkcd.com/')
while xkcd_request.status_code == 200:
    xkcd_soup = bs4.BeautifulSoup(xkcd_request.text, 'html.parser')
    title = xkcd_soup.select('#ctitle')
    print(title[0].text)
    prev = xkcd_soup.select('#middleContainer > ul:nth-child(2) > li:nth-child(2) > a')
    xkcd_request = requests.get(f'''https://xkcd.com{prev[0].get('href')}''')
