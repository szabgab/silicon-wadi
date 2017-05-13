
List of hi-tech companies in Israel along with the location of their development offices
and the list of technologies they are using.

# Contribution

Before committing, make sureyou tidy the json file and the run our sanity tests:
(Using Python 3)

```
pip install pytest
./bin/tidy_json.py
pytest
```

# Data

Companies are in the [companies.json](data/companies.json). 

Each company has an entry with one or more offices. See [skeleton.json](data/skeleton.json).

"technologies" should be a list of technologies used in the company. E.g. JavaScript, Python, Java, Docker, MySQL, AngularJS.
The list of technologies can be found in the [technologie.json](data/technologies.json) file. It serves us a way to check we don't
make typos and we don't have different spellings of the same thing.  Update that file too if you'd like to list another technology.

https://www.gps-coordinates.net/ can be used to convert addresses to coordinates.

"area" is one of the keys from the [areas.json](data/areas.json) file.

# Demo application:

http://wadi.szabgab.com/

