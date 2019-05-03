import json

with open('gdp_json.json') as f:
    reader = json.load(f)
    
for k in reader:
    if k['Year'] == 2010:
        print(k['Country Name'])
