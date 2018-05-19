#!/usr/bin/env python3
import json
import glob

# format the json files
data_dir = 'html/data/'

def tidy(test = False):
    for filename in glob.glob(data_dir + "*.json") + glob.glob(data_dir + 'c/' + "*.json"):
        #print(filename)
        with open(filename) as fh:
            json_str = fh.read()
            data = json.loads(json_str)

#        if filename == data_dir + 'companies.json':
#            data.sort(key = lambda c: c['name'])
        if filename == data_dir + 'technologies.json':
            data.sort()

        new_json_str = json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))
        if test:
            assert new_json_str == json_str, filename + " is not tidy. Run 'python bin/tidy_json.py'"
            continue

        with open(filename, 'w') as fh:
            fh.write(new_json_str)
            

if __name__ == "__main__":
    tidy()

# vim: expandtab
