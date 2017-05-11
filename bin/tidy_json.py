#!/usr/bin/env python3
import json
import glob

# format the json files

for filename in glob.glob("data/companies.json"):
    with open(filename) as fh:
        data = json.load(fh)
    with open(filename, 'w') as fh:
        data.sort(key = lambda c: c['name'])
        json.dump(data, fh, sort_keys=True, indent=4, separators=(',', ': '))

# vim: expandtab
