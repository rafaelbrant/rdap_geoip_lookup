# Python Challenge to perform RDAP and GeoIP Lookups

This project will get a unstructured txt file with IPs and perform a lookup operation using The Registration Data Access Protocol - RDAP and GeoIP.
The results will be saved separately on json files on the project folder. 
It uses the free apis 'https://www.rdap.net' and http://www.geoplugin.net/

## Requirements
The only external requirements are:
```
pip3 install requests==2.22.0
pip3 install pytest-mock
```

## Running from the command line

To perform the lookups we must provide the txt file and the services we want to use as a flag.

To perform RDAP lookup:
```
python3 main.py file.txt --services rdap
```
To perform a GeoIP lookup:
```
python3 main.py file.txt --services geoip
```
To perform both lookups:
```
python3 main.py file.txt --services geoip rdap
```

## Running tests
```
python3 -m pytest tests/
```

