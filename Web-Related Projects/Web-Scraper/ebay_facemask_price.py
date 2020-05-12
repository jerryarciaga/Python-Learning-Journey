#!/usr/bin/python

# Face mask price finder
import bs4, requests, re

facemask_request = requests.get('''https://www.ebay.com/sch/i.html?_from=R40&_t
rksid=p2380057.m570.l1313.TR12.TRC2.A0.H0.Xface+mask.TRS0&_nkw=face+mask
&_sacat=0''')

facemask_prices = bs4.BeautifulSoup(facemask_request.text, 'html.parser')

for i in range(7, 100):
    try:
        price_data = facemask_prices.select("#srp-river-results > ul > li:nth-child("+
        str(i) +") > div > div.s-item__info.clearfix > div.s-item__details.clearfix > div:nth-child(1) > span")
        priceRegex = re.compile(r'''
            (
            (\$)
            (\d)+
            (\.)
            (\d)+
            )
            ''', re.VERBOSE)

        price = priceRegex.findall(str(price_data))
        print(price[0][0])
    except:
        pass

