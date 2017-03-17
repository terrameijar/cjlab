#! /usr/bin/env python3
# 10.py --Title of the highest paid California city government position in 2010


import requests
import os.path
import csv
from shutil import unpack_archive
local_data_dir = "/tmp/capublicpay"
years = range(2015, 2016)  # Just 2015, useful for longer ranges


def foosalary(row):
    return float(row['Total Wages']) if row['Total Wages'] else 0

for year in years:
    fname = '%s_City' % year
    url = 'http://publicpay.ca.gov/Reports/RawExport.aspx?file=%s.zip' % fname
    local_zip_fname = os.path.join("/tmp", fname + '.zip')
    local_csv_fname = os.path.join(local_data_dir, fname + '.csv')

    if not os.path.exists(local_zip_fname):
        print("Downloading", url, 'to', local_zip_fname)
        data = requests.get(url).content
        with open(local_zip_fname, 'wb') as f:
            f.write(data)
    # done downloading, now unzip files
    print("Unzipping", local_zip_fname, 'to', local_data_dir)
    unpack_archive(local_zip_fname, local_data_dir, format='zip')

    with open(city_data, encoding='latin-1') as f:
        data = list(csv.DictReader(f.readlines()))
        topitem = max(data, key=foosalary)
        print(topitem['Entity Name'], topitem['Department / Subdivision'],
              topitem['Position'], topitem['Total Wages'])