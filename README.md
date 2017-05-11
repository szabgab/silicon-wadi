List of hi-tech companies in Israel along with the location of their development offices
and if possible along with a list of technologies they are using.

Companies are in the 'companies.json'. Before committing, please run `./tidy_json.py`.
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
                "phone" : ""
            }
        ]
    },
```

Where "technologies" should be a list of technologies used in the company. E.g. JavaScript, Python, Java, Docker, MySQL, AngularJS.

(TODO: add a definitive list of technologies and check the submissions agains that list)

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

