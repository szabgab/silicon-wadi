# Silicon Wadi

List of hi-tech companies in Israel along with the location of their development offices
and the list of technologies they are using.

## Contribution

Install [uv](https://docs.astral.sh/uv/getting-started/installation/).

Before committing, make sure you tidy the JSON file and the run our sanity tests:

```
uv run python bin/tidy_json.py
uv run pytest
```

## Data

Companies are stored in the `html/data/c` directory.

Each company has a file with one or more offices. See [skeleton.json](html/data/skeleton.json).

Before deploying the new data set we generate the html/data/companies.json file using the following command:

```
uv run python bin/collector.py
```


`technologies` should be a list of technologies used in the company. E.g. JavaScript, Python, Java, Docker, MySQL, AngularJS.
The list of technologies can be found in the [technologies.json](html/data/technologies.json) file. The list serves us a way to check we don't make typos and we don't have different spellings of the same thing. Update that file too if you'd like to include another technology.

https://www.gps-coordinates.net/ can be used to convert an `address` to `coordinates`.

`area` is one of the keys from the [areas.json](html/data/areas.json) file. We use this field to try to cluster the offices.


## Local development

run

```
uv run python bin/static_server.py
```

and then visit: http://localhost:8000/

## Update coordinates

Once we have the address of an office and save it in the json file of the company we can run the following code to fetch
the coordinates and update them in the json file:

```
bin/update_coordinates.py
```

In order for this to work we need to create a file called `~/google.cfg` and save in it:

```
[maps]
api_key=
```

Where the value of the api_key comes from https://console.cloud.google.com/google/maps-apis/apis/geocoding-backend.googleapis.com/metrics


## Demo application:

http://wadi.szabgab.com/

