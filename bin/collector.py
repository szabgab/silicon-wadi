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
    return companies

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

    companies = collect_data()
#    for company in companies:
#        print(company)
#        exit()

    html_path = "html"
    render(
        full_path=os.path.join(html_path, "index.html"),
        template="index.html",
        today=today,
        companies=companies,
    )

