newt_hft
--------

python module to transfer QA output files of STAR's new HFT detector from
RCF@RHIC to http://portal.nersc.gov/project/star/hft/ (h5ai apache index) via
NERSC's NEWT API (https://newt.nersc.gov/)

#### Usage

```
# set/export environment variables NEWT_USER and NEWT_PWD with NIM NERSC credentials
$ git clone https://github.com/tschaume/newt_hft.git
$ virtualenv-2.7 env
$ source env/bin/activate # needs to be done for every new login shell
$ pip install -r requirements.txt
$ ./newt_hft.py -h
$ ./newt_hft.py output/2014/034/15034081 # or
$ ./newt_hft.py --log output/2014/034/15034081 # to show log output
```

command line argument <basepath>: (e.g. output/2014/034/15034081)

- base path of output files for respective RunId
- is assumed to end in YYYY/DDD/RUN (no extension)
- {.pdf,.root} will be appended and copied to according location on PDSF
- any part of the path before YYYY/DDD/RUN will be ignored

#### ToDo

- test on RCF (beind proxy!)
- log to file not console
