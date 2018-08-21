#!/usr/bin/env python3
# lucky.py - Opens several Google search results.
# Usage: python3 lucky.py <search term>

import requests
import sys
import bs4
import webbrowser

print('Googling...')           # Display text while downloading the Google page
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status

soup = bs4.BeautifulSoup(res.text)

linkElems = soup.select('.r a')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))
