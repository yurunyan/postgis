import json

path = r"G:\data\geography\test\N02-16_GML\N02-16_Station.geojson"
with open(path, 'r', encoding='utf8') as f:
    data = f.read()
data = json.loads(data)
for x in data["features"]:
    if x['properties']['運営会社'] == '京王電鉄':
        print(x["properties"]["駅名"])
        print(x["geometry"]["coordinates"])
