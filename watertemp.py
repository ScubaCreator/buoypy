import requests
import json

LJurl = "https://api.tidesandcurrents.noaa.gov/api/prod/datagetter"
LJheaders = {
"date":"latest",
"station":"9410230",
"product":"water_temperature",
"datum":"STND",
"units":"english",
"time_zone":"lst_ldt",
"format" :"json"
}

resp = requests.get(LJurl, params=LJheaders)
data = resp.json()

LJtemp = (data['data'][0]['v'])


LAurl = "https://api.tidesandcurrents.noaa.gov/api/prod/datagetter"
LAheaders = {
"date":"latest",
"station":"9410660",
"product":"water_temperature",
"datum":"STND",
"units":"english",
"time_zone":"lst_ldt",
"format" :"json"
}

resp = requests.get(LJurl, params=LJheaders)
data = resp.json()
LAtemp = (data['data'][0]['v'])


FLJtemp = float(LJtemp)
FLAtemp = float(LAtemp)


print((FLJtemp+FLAtemp) / 2)


