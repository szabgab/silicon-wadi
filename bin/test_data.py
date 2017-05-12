import json
import tidy_json

def test_data():
    assert True
    with open('data/companies.json') as fh:
        companies = json.load(fh)
    with open('data/technologies.json') as fh:
        technologies = set(json.load(fh))

    for c in companies:
        if 'technologies' in c:
            for t in c['technologies']:
                assert t in technologies
def test_tidy():
    tidy_json.tidy(test = True)

# vim: expandtab

