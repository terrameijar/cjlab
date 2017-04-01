#! /usr/bin/env python3
import os.path
import unittest
import requests
from xlrd import open_workbook, cellname
from bs4 import BeautifulSoup
from shutil import unpack_archive


# How much did the state of California collect in property taxes,
# according to the U.S. Census 2013 Annual Survey of State
# Government Tax Collections?

# url = http://www.census.gov/govs/statetax/historical_data.html
link = 'https://www.census.gov/govs/statetax/historical_data.html'
filename = 'STC_Historical_DB.xls'
dataset_zipfile = None
temp_dir = '/tmp'
local_data_dir = '/tmp/state_tax_collections/'  # For extracted data
# data = 'http://www2.census.gov/govs/statetax/stcfy16.zip'

# Get the dataset from url
response = requests.get(link)
soup = BeautifulSoup(response.text, 'lxml')
# URL of the dataset zip file
data = soup.select('div.hi-lite ul li a')[0]['href']
base_filename = os.path.basename(data)

# Save the dataset to a temp folder
local_zipname = os.path.join(temp_dir, base_filename)
# we will cache the download
if not os.path.exists(local_zipname):
    print('Downloading dataset from %s to %s' % (link, local_zipname))
    zipfile_data = requests.get(data).content
    with open(local_zipname, 'wb') as f:
        f.write(zipfile_data)

    # Downloaded, now unpack the dataset
    print('Unzipping %s to %s' % (local_zipname, local_data_dir))
    unpack_archive(local_zipname, temp_dir, format='zip')
# Open the statistics dataset
stats_db_doc = os.path.join(local_data_dir, "STC_Historical_DB.xls")
work_book = open_workbook(stats_db_doc)
work_sheet = work_book.sheet_by_index(0)
# Get property tax data for State of California
CO_property_tax = work_sheet.cell_value(rowx=110, colx=5)
CO_year = work_sheet.cell_value(rowx=110, colx=0)
print("California collected ${0} in property taxes in 2013"
      .format(CO_property_tax))
