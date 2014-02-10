#!/usr/bin/env python

from requests_toolbelt import MultipartEncoder
import requests, logging, argparse, sys
from fnmatch import fnmatch
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

  # get paths, out path and filebase
  path_arr = args.basepath.split('/')
  out_path = '/'.join(path_arr[-3:-1]) + '/'
  filebase = path_arr[-1]
  logging.debug('%s %s' % (out_path, filebase))

  # make output dir on remote
  r_mkdir = s.post(getEndpoint('command'), {
    'executable': '/bin/mkdir -pv ' + HFTDIR + out_path
  })
  logging.debug(r_mkdir.content)

  # transfer files
  xfer_to = getEndpoint('file', True) + out_path
  logging.debug(xfer_to)
  for ext in ['.pdf', '.root']:
    with open(args.basepath + ext, 'rb') as fd:
      m = MultipartEncoder([('field', 'foo'), ('file', fd)])
      #('file', (filebase + ext, open(args.basepath + ext, 'rb'), 'text/plain')
      #logging.debug(m.to_string())
      r_xfer = s.put(xfer_to, data = m, headers={'Content-Type': m.content_type})
      #filebase + ext: open(args.basepath + ext, 'rb')
      logging.debug(r_xfer.content)

  sys.exit(0)

  # clean up remote
  r_ls = s.post(getEndpoint('command'), {
    'executable': '/bin/ls ' + HFTDIR + out_path
  })
  logging.debug(r_ls.content)
  newt_rm = r_ls.json()['output'].split('\n')
  for f in newt_rm:
    if fnmatch(f, 'newt_*'):
      r_clean = s.post(getEndpoint('command'), {
        'executable': '/bin/rm ' + HFTDIR + out_path + f
      })
      logging.debug(r_clean.content)
