#!/usr/bin/env python

import requests, os

# session and newt base url
s = requests.Session()
api = 'https://newt.nersc.gov/newt/'

# authenticate
username = os.environ['NEWT_USER']
password = os.environ['NEWT_PWD']
payload = 'username=' + username + '&password=' + password
s.post(api + 'auth', data = payload)

# list hft file contents
endpoint = api + 'file/pdsf/project/projectdirs/star/www/hft'
r = s.get(endpoint)
print r.json()
