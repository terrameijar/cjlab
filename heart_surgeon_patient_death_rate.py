#! /usr/bin/env/ python

import requests
url = 'https://health.data.ny.gov/resource/dk4z-k3xb.json'
search_string = 'Rate significantly higher than Statewide Rate'
data = requests.get(url).json()
records = [r for r in data if search_string in r['comparison_results']]
print len(records)