newt_hft
--------

python module to transfer QA output files of STAR's new HFT detector from
RCF@RHIC to http://portal.nersc.gov/project/star/hft/ (h5ai apache index) via
NERSC's NEWT API (https://newt.nersc.gov/)

```
# set/export environment variables NEWT_USER and NEWT_PWD with NIM NERSC credentials
$ git clone https://github.com/tschaume/newt_hft.git
$ virtualenv-2.7 env
$ source env/bin/activate # needs to be done for every new login shell
$ pip install -r requirements.txt
$ ./newt_hft.py -h
```

TODO:

- test on RCF (beind proxy!)
- log to file not console
