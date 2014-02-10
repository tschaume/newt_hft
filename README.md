newt_hft
--------

python module to transfer QA output files of STAR's new HFT detector from
RCF@RHIC to http://portal.nersc.gov/project/star/hft/ (h5ai apache index) via
NERSC's NEWT API (https://newt.nersc.gov/)

```
# set environment variables NEWT_USER and NEWT_PWD with NIM NERSC credentials
# clone repo
$ virtualenv-2.7 env
$ source env/bin/activate
$ pip install -r requirements.txt
$ ./newt_hft.py -h
```

TODO:

- test on RCF
- log to file not console
