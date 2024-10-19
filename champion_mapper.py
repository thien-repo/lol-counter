import requests 

url = 'https://ddragon.leagueoflegends.com/api/versions.json'

res = requests.get(url)
if res.status_code != 200:
    print(res.text)
    exit(1)

import json 

data = json.loads(res.text)
ver = data[0]
champion_url= f'https://ddragon.leagueoflegends.com/cdn/{ver}/data/en_US/champion.json'

res = requests.get(champion_url)
if res.status_code != 200:
    print(res.text)
    exit(1)

data = json.loads(res.text)['data']
with open('templates/champions.json', 'w') as file:
    champion_dict = {}
    for info in data:
        champion_dict[ data[info]['key'] ] =  info
    json.dump(champion_dict, file)

