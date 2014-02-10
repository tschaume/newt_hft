#!/usr/bin/env python

import requests, os, logging, argparse
from config import *

if __name__ == '__main__':

  parser = argparse.ArgumentParser()
  parser.add_argument(
    "basepath", help="""
    base path of output files for respective RunId,
    is assumed to end in YYYY/DDD/RUN (no extension),
    {.pdf,.root} will be appended and copied to according location on PDSF,
    any part of the path before YYYY/DDD/RUN will be ignored
    """)
  parser.add_argument("--log", help="show log output", action="store_true")
  args = parser.parse_args()
  loglevel = 'DEBUG' if args.log else 'WARNING'
  logging.basicConfig(
    format='%(message)s', level=getattr(logging, loglevel)
  )

  s = requests.Session()
  username = os.environ['NEWT_USER']
  password = os.environ['NEWT_PWD']
  payload = 'username=' + username + '&password=' + password
  r_auth = s.post(API + 'auth', data = payload)
  logging.debug(r_auth.content)
  r_list = s.get(ENDPOINT)
  logging.debug(r_list.content)
  xfer_to = '/'.join([ENDPOINT] + args.basepath.split('/')[-3:])
  logging.debug(xfer_to)

