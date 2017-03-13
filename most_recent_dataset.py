#! /usr/bin/env python
# Name of the most recently added dataset

from lxml import html
import requests
response = requests.get('http://catalog.data.gov/dataset?\
    q=&sort=metadata_created+desc')
doc = html.fromstring(response.text)
title = doc.cssselect('h3.dataset-heading')[0].text_content()
print title.strip()