#! /usr/bin/env python3

# From 2010 to 2013, the change in median cost of health, 
# dental and vision coverage for Carlifornia city employeesself.
# shutil.unpack_archive requires python 3.6+


import os
import requests
import csv
from shutil import unpack_archive
from statistics import median

local_data_dir = '/tmp/capublicpay'
base_url = 'http://publicpay.ca.gov/Reports/RawExport.aspx?file='
years = (2010, 2013)

medians = []
for year in years:
    base_file_name = '%s_City.zip' % year
    url = base_url + base_file_name
    local_zname = '/tmp/' + base_file_namer
    # this is such a massive file that we should cache the download
    if not os.path.exists(local_zname):
        print('Downloading', url, 'to', local_zname)
        data = requests.get(url).content
        with open(local_zname, 'wb') as f:
            f.write(data)
    # done downloading, no unzip files
    print('Unzipping', local_zname, 'to', local_data_dir)
    unpack_archive(local_zname, local_data_dir, format = 'zip')
    # each zip extracts a file named YEAR_City.csv
    csv_name = local_data_dir + '/' + base_file_name.replace('zip', 'csv')
    # calculate median
    with open(csv_name, encoding = 'latin-1') as f:
        cx = list(csv.DictReader(f.readlines()[4:]))
        mx = median([float(row['Health Dental Vision']) for row in cx if row['Health Dental Vision']])
        print("Median for  %s" % year, mx)
        medians.append(mx)

print(medians[-1] - medians[0])