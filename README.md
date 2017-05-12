
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

"area" is one of the following areas. (TODO: unify the words used in the field. Create a JSON file of all the areas with descriptions where there might be ambiguity. Script to verify we use only the arease defined in that file.)

# Areas

* Airport City
* Beer Sheva  http://www.atp-israel.com/
* Cesaria
* Haifa - MATAM
* Herzelia Pituach
* Hod HaSharon
* Jerusalem - Malcha
* Jerusalem - Har Hotzvim
* Ness Ziona
* Netanya – Poleg
* Omer = Omer Industrial Park
* Petach Tikva - Kiryat Arie
* Petach Tikva - other areas
* Raanana
* Rehovot
* Rosh HaAyin
* Tefen = Tefen Industrial Park
* Tel Aviv - Kiryat Atidim
* Tel Aviv - Namal
* Tel Aviv - Ramat HaHayal
* Yokneam

# Demo application:

http://wadi.szabgab.com/

