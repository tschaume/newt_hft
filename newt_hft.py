#!/usr/bin/env python

import requests, logging, argparse
from config import *

def getEndpoint(resource, dir = False):
  return API + resource + SYSTEM + (HFTDIR if dir else '')

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

  # get session and authenticate
  s = requests.Session()
  r_auth = s.post(API + 'auth', CREDS)
  logging.debug(r_auth.content)

  # get paths and list of files to transfer
  path_arr = args.basepath.split('/')
  out_path = '/'.join(path_arr[-3:-1])
  filebase = path_arr[-1]
  files = dict(
    (filebase + ext, open(args.basepath + ext, 'rb'))
    for ext in ['.pdf', '.root']
  )
  logging.debug(files)

  # make output dir on remote
  r_mkdir = s.post(getEndpoint('command'), {
    'executable': '/bin/mkdir -p ' + HFTDIR + out_path
  })
  logging.debug(r_mkdir.content)

  # transfer files
  xfer_to = getEndpoint('file', True) + out_path + '/'
  logging.debug(xfer_to)
  r_xfer = s.put(xfer_to, files=files)
  logging.debug(r_xfer.content)

