import json
import re
import os
import pytest

import tidy_json
from collector import collect_data, data_dir

def test_data():
    assert True
    collect_data()
    with open(os.path.join(data_dir, 'companies.json')) as fh:
        companies = json.load(fh)
    with open(os.path.join(data_dir, 'technologies.json')) as fh:
        technologies = set(json.load(fh))
    with open(os.path.join(data_dir, 'areas.json')) as fh:
        areas = set(json.load(fh))

    # Each company must have a 'name', and a 'url'.
    for c in companies:
        assert 'name' in c and c['name']
        assert 'url' in c and c['url']
        assert re.search(r'https?://', c['url']), 'Invalid URL "{}" for company {}'.format(c['url'], c['name'])

    # Verify that there are no two addresses with the exact same coordinates.
    # So we'll have separate markers for each company.
    coordinates = {}
    for c in companies:
        for office in c['offices']:
            assert 'coordinates' in office, "Coordinates missing from " + c['name']
            if 'coordinates' in office:
                coord = (office['coordinates']['lat'], office['coordinates']['lng'])
                assert 29.48216448377731 < office['coordinates']['lat'] < 33.33259353927003, 'Expected to be within Israel South - North for company {}'.format(c['name'])
                assert 34.27734375       < office['coordinates']['lng'] < 35.90057373046875, 'Expected to be within Israel West  - East for company {}'.format(c['name'])
                if coord in coordinates:
                    raise Exception("Duplicate coordinates:\n{}\n{} ({})".format(coordinates[coord]['name'], c['name'], office['address']))
                coordinates[coord] = c

    # Verify the areas:
    for c in companies:
        for office in c['offices']:
            assert 'area' in office and office['area'] != '', 'Missing area for {}'.format(c['name'])
            if 'area' in office and office['area'] != '':
                assert office['area'] in areas


    # Verify the format of phone numbers:
    for c in companies:
        for office in c['offices']:
            if 'phone' in office and office['phone'] != '':
                assert re.search(r'^\+972-\d\d?-\d\d\d-?\d\d\d\d$', office['phone'])

    # Each technology is listed in the data_dir + technologies.json
    # Avoid typo, and different spellings of the same technology.
    for c in companies:
        if 'technologies' in c:
            for t in c['technologies']:
                assert t in technologies

@pytest.mark.skipif('TRAVIS' in os.environ and os.environ['TRAVIS_PULL_REQUEST'] != 'false', reason="Pull request might be 'dirty'")
def test_tidy():
    tidy_json.tidy(test = True)

# vim: expandtab

