#!/usr/bin/env python3
import json
import glob

# format the json files

def tidy(test = False):
    for filename in glob.glob("data/*.json"):
        #print(filename)
        with open(filename) as fh:
            json_str = fh.read()
            data = json.loads(json_str)

        if filename == 'data/companies.json':
            data.sort(key = lambda c: c['name'])
        if filename == 'data/technologies.json':
            data.sort()

        new_json_str = json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))
        if test:
            assert new_json_str == json_str, filename + " is not tidy. Run ./bin/tidy_json.py"
            continue

        with open(filename, 'w') as fh:
            fh.write(new_json_str)
            

if __name__ == "__main__":
    tidy()

# vim: expandtab
