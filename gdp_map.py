import json
from pygal.maps.world import COUNTRIES
import pygal.maps.world

gdp_dict = {}

with open('gdp_json.json') as f:
    reader = json.load(f)
    
for k in reader:
    if k['Year'] == 2016:
        country_name = k['Country Name']
        gdp = int(k['Value'])
        for country_code, country in COUNTRIES.items():
            if country_name == country:
                code = country_code
                gdp_dict[code] = gdp
                
gdp_dict_1, gdp_dict_2, gdp_dict_3 = {}, {}, {}
for cc, gdp in gdp_dict.items():
    if gdp < 5000000000:
        gdp_dict_1[cc] = round(gdp/1000000000)
    elif gdp < 50000000000:
        gdp_dict_2[cc]  = round(gdp/1000000000)
    else:
        gdp_dict_3[cc] = round(gdp/1000000000)

wm = pygal.maps.world.World()
wm.title = '2016 World GDP'    
wm.add('0-5bn', gdp_dict_1)
wm.add('5-50bn', gdp_dict_2)
wm.add('>50bn', gdp_dict_3)

wm.render_to_file('2016_gdp.svg')        
