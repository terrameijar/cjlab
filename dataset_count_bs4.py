#! /usr/bin/env python
# Counts number of datasets currently listed on data.gov
# using Beautiful Soup

import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.data.gov/')
soup = BeautifulSoup(response.text, 'lxml')
link_text = soup.small.a.string
print link_text