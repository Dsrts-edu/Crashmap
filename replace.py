import json
with open('/Users/mike/crashmap/fatals2019.geojson') as f:
    data = json.load(f)

for item in data['features']:
    for prop in item:
        print(prop)
    

##with open('newFatals2019.json', 'w') as f:
  ##  json.dump(data, f)