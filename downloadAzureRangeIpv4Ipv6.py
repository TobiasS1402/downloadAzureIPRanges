import requests
import json
import re

#Download Azure ip list https://www.microsoft.com/en-us/download/details.aspx?id=56519
url = requests.get('https://download.microsoft.com/download/7/1/D/71D86715-5596-4529-9B13-DA13A5DE5B63/ServiceTags_Public_20220131.json') #all public ip-ranges in azure
txt = url.text
data = json.loads(txt)

list = []    

for x in data["values"]:
    for y in x["properties"]["addressPrefixes"]:
        list.append(y)

file=open('AzureIPRanges.txt', 'w+')
for iprange in list:
    file.writelines(iprange+'\n')

file.close()
