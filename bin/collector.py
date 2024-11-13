import glob
import os
import json
import datetime
import jinja2

root = os.path.dirname(os.path.dirname(__file__))
data_dir = os.path.join(root, 'html', 'data')

def collect_data():
    companies = []
    for filename in glob.glob(os.path.join(data_dir, 'c', '*.json')):
        #print(filename)
        with open(filename) as fh:
            d = json.load(fh)
            d['filename'] = filename
            companies.append(d)
    companies.sort(key = lambda c: c['name'])
    with open(os.path.join(data_dir, 'companies.json'), 'w') as fh:
       new_json_str = json.dumps(companies, sort_keys=True, indent=4, separators=(',', ': '))
       fh.write(new_json_str)
    return list(filter(lambda company: 'disabled' not in company or not company['disabled'], companies))

def render(full_path, template, **args):
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    templates_dir = os.path.join(root, "templates")
    #print(templates_dir)
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(templates_dir), autoescape=True)

    html_template = env.get_template(template)
    html = html_template.render(**args)

    dir_path = os.path.dirname(full_path)
    os.makedirs(dir_path, exist_ok=True)

    with open(full_path, "w") as fh:
        fh.write(html)


if __name__ == '__main__':
    now = datetime.datetime.now()
    today = now.strftime('%Y.%m.%d')
    areas = {}

    companies = collect_data()
    for company in companies:
        # print(company)
        for office in company['offices']:
            #print(office)
            area_name = office['area']
            area = area_name.lower().replace(' ', '-')

            if area not in areas:
                areas[area] = {
                    "name": area_name,
                    "companies": []
                }
            areas[area]["companies"].append(company)

    html_path = "html"
    render(
        full_path=os.path.join(html_path, "index.html"),
        template="index.html",
        today=today,
        companies=companies,
        location="Israel",
    )

    render(
        full_path=os.path.join(html_path, "area", "index.html"),
        template="area.html",
        today=today,
        areas=areas,
    )

    os.makedirs(os.path.join(html_path, "area"), exist_ok=True)

    for area, data in areas.items():
        render(
            full_path=os.path.join(html_path, "area", f"{area}.html"),
            template="index.html",
            today=today,
            area=area,
            location=data["name"],
            companies=data["companies"],
        )


