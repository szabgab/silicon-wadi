import json
import re

import tidy_json

def test_data():
    assert True
    with open('data/companies.json') as fh:
        companies = json.load(fh)
    with open('data/technologies.json') as fh:
        technologies = set(json.load(fh))
    with open('data/areas.json') as fh:
        areas = set(json.load(fh))

    # Verify that there are no two addresses with the exact same coordinates.
    # So we'll have separate markers for each company.
    coordinates = {}
    for c in companies:
        for office in c['offices']:
            if 'coordinates' in office:
                coord = (office['coordinates']['lat'], office['coordinates']['lng'])
                if coord in coordinates:
                    raise Exception("Duplicate coordinates:\n" + coordinates[coord]['name'] + "\n" + c['name'])
                coordinates[coord] = c

    # Verify the areas:
    for c in companies:
        for office in c['offices']:
            #assert 'area' in office and office['area'] != '', "Missing area for " + c['name']
            if 'area' in office and office['area'] != '':
                assert office['area'] in areas


    # Verify the format of phone numbers:
    for c in companies:
        for office in c['offices']:
            if 'phone' in office and office['phone'] != '':
                assert re.search(r'^\+972-\d\d?-\d\d\d-?\d\d\d\d$', office['phone'])

    # Each technology is listed in the data/technologies.json
    # Avoid typo, and different spellings of the same technology.
    for c in companies:
        if 'technologies' in c:
            for t in c['technologies']:
                assert t in technologies

def test_tidy():
    tidy_json.tidy(test = True)

# vim: expandtab

