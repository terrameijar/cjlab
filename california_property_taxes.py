#! /usr/bin/env python
import os.path
import unittest
import requests
from bs4 import BeautifulSoup

# How much did the state of California collect in property taxes, 
# according to the U.S. Census 2013 Annual Survey of State 
# Government Tax Collections?

# url = http://www.census.gov/govs/statetax/historical_data.html
link = 'https://www.census.gov/govs/statetax/historical_data.html'
filename = 'STC_Historical_DB.xls'
dataset_zipfile = None
temp_dir = '/tmp'
#data = 'http://www2.census.gov/govs/statetax/stcfy16.zip'

# TODO: 1) Get the dataset from url
response = requests.get(link)
soup = BeautifulSoup(response.text, 'lxml')
# URL of the dataset zip file
data = soup.select('div.hi-lite ul li a')[0]['href']
base_filename = os.path.basename(data)
#print(base_filename)  # stcfy16.zip

# TODO: 2) Save the dataset to a temp folder

local_zipname = os.path.join(temp_dir, base_filename)
# we will cache the download because of it's sheer size
if not os.path.exists(local_zipname):
    print('Downloading dataset from %s to %s' % (link, local_zipname))
    zipfile_data = requests.get(data).content
    with open(local_zipname, 'wb') as f:
        f.write(zipfile_data)

# TODO: 3) Unpack the dataset
# TODO: 4) Open the statistics dataset
# TODO: 5) Get property tax data for State of California
# TODO: **Write the using TDD**