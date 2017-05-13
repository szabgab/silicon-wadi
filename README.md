
List of hi-tech companies in Israel along with the location of their development offices
and the list of technologies they are using.

Companies are in the [companies.json](data/companies.json). Before committing, please run `./tidy_json.py`.

Each company has the following entry:


```
    {
        "name": "",
        "url": "",
        "technologies" : [],
        "offices": [
            {
                "area" : "",
                "address": "",
                "phone" : "",
                "coordinates": {
                    "lat": 0,
                    "lng": 0
                }
            }
        ]
    },
```

"technologies" should be a list of technologies used in the company. E.g. JavaScript, Python, Java, Docker, MySQL, AngularJS.
The list of technologies can be found in the [technologie.json](data/technologies.json) file. It serves us a way to check we don't
make typos and we don't have different spellings of the same thing.  Update that file too if you'd like to list another technology.

https://www.gps-coordinates.net/ can be used to convert addresses to coordinates.

"area" is one of the keys from the [areas.json](data/areas.json) file.

TODO add these areas:
* Cesaria
* Jerusalem - Malcha
* Ness Ziona
* Netanya – Poleg
* Petach Tikva - Kiryat Arie
* Petach Tikva - other areas
* Raanana
* Rosh HaAyin
* Yokneam

TODO: require name and address for each office
TODO: require area for each office
TODO: require coordinates for each office

# Contribution

Using Python 3 make sure our data sanity tests pass:

```
pip install pytest
pytest
```

# Demo application:

http://wadi.szabgab.com/

