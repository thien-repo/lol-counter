import requests
import json
from bs4 import BeautifulSoup

url = "https://u.gg/api"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
    "Content-Type": "application/json"
}

def get_match_history(content):
    return content['data']['fetchPlayerMatchSummaries']['matchSummaries']

def get_player_match_info(m):
    return  (m['win'],
            (m['kills'], m['deaths'], m['assists']), 
            m['visionScore'],
            m['gold'],
            m['cs'],
            m['championId'],
            m['queueType'])


with open('query.json', 'r') as payload:
    data = json.load(payload)
    res = requests.post(url, headers=headers,json=data)
    if res.status_code == 200:
        match_history = get_match_history(json.loads(res.text))
        player_name = 'Reap'
        for m in match_history:
            win, kda, vs, gold, cs, champid, qtype = get_player_match_info(m)
            print(win, kda, vs, gold, cs, champid, qtype)
            