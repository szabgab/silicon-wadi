import glob
import os
import json

data_dir = 'html/data/'

def collect_data():
    companies = []
    for filename in glob.glob(os.path.join(data_dir, 'c/*.json')):
        print(filename)
        with open(filename) as fh:
            d = json.load(fh)
            companies.append(d)
    companies.sort(key = lambda c: c['name'])
    with open(data_dir + 'companies.json', 'w') as fh:
       new_json_str = json.dumps(companies, sort_keys=True, indent=4, separators=(',', ': '))
       fh.write(new_json_str)
 
if __name__ == '__main__':
    collect_data()
