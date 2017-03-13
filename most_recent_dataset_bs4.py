#! /usr/bin/env python
# Name of the most recently added dataset

import requests
from bs4 import BeautifulSoup


response = requests.get('http://catalog.data.gov/dataset?\
    q=&sort=metadata_created+desc')
soup = BeautifulSoup(response.text, 'lxml')
title = soup.select('h3.dataset-heading > a')[0].string
print title