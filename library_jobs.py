#! /usr/bin/env python
# The number of librarian related job positions that the
# federal government is currently hiring for.

import requests
from bs4 import BeautifulSoup


# via http://www.opm.gov/policy-data-oversight/classification\
# -qualifications/general-schedule-qualification-standards/#url=List-by-Occupational-Series

library_series = 1410
response = requests.get('http://usajobs.gov/JobSearch/Search/GetResults?', params =
    {'series': library_series})
response.raise_for_status()
soup = BeautifulSoup(response.text, 'lxml')
total_jobs = soup.select('span.pageset.pager-totalRecords')[0].string.strip()
print "The number of open librarian jobs is %s" % total_jobs