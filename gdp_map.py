import json
from pygal.maps.world import COUNTRIES
import pygal.maps.world

gdp_dict = {}

with open('gdp_json.json') as f:
    reader = json.load(f)
    
for k in reader:
    if k['Year'] == 2016:
        country_name = k['Country Name']
        gdp = k['Value']
        for country_code, country in COUNTRIES.items():
            if country_name == country:
                code = country_code
                gdp_dict[code] = int(float(gdp))

wm = pygal.maps.world.World()
wm.title = '2016 World GDP'    
wm.add('Countries', gdp_dict)
wm.render_to_file('2016_gdp.svg')        
