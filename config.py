import os
# NOTE: don't forget trailing slash in urls!
API = 'https://newt.nersc.gov/newt/'
SYSTEM = '/pdsf'
HFTDIR = '/project/projectdirs/star/www/hft/'
# NEWT API credentials
CREDS = {
  "username": os.environ['NEWT_USER'],
  "password": os.environ['NEWT_PWD']
}
