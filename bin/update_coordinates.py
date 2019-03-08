#!/usr/bin/env python3
import os
import json
import sys
import requests
import configparser

cfg = configparser.ConfigParser()
cfg.read(os.path.join(os.path.expanduser('~'), 'google.cfg'))
api_key = cfg['maps']['api_key']


def get_coordinates(address):
    url = 'https://maps.googleapis.com/maps/api/geocode/json?address=' + address + '&key=' + api_key
    print(url)
    resp = requests.get(url)
    print(resp.status_code)
    print(resp.text)

    data = resp.json()
    return data['results'][0]['geometry']['location']

#print(sys.argv)
if (len(sys.argv) != 2):
    exit("Usage: {} html/data/c/company.json".format(sys.argv[0]))

filename = sys.argv[1]
with open(filename) as fh:
    data = json.load(fh)
for off in data['offices']:
    print(off['address'])
    coord = get_coordinates(off['address'])
    print(coord)
    off['coordinates'] = coord
new_json_str = json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))
with open(filename, 'w') as fh:
    fh.write(new_json_str)

