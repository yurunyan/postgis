import json
import simplekml
import numpy as np

kml = simplekml.Kml()

path = r"G:\data\geography\test\N02-16_GML\N02-16_Station.geojson"
with open(path, 'r', encoding='utf8') as f:
    data = f.read()
data = json.loads(data)
for x in data["features"]:
    if x['properties']['運営会社'] == '京王電鉄':
        sta = x["geometry"]["coordinates"]
        sta_name = x["properties"]["駅名"]

        print(sta)
        
        kml.newlinestring(name=sta_name, coords=sta)

        sta2 = np.mean(sta, axis=0).tolist()
        print(sta2)
        print(type(sta2))

        p = kml.newpoint(name=sta_name)
        p.coords = [(sta2[0], sta2[1])]

        a=[(sta2[0], sta2[1])]
        print(type(a))
        print(a)

kml.save("keio.kml")

        
