import json
from bs4 import BeautifulSoup
from dataclasses import dataclass


@dataclass
class MatchHistory:
    win: bool
    kills: int
    deaths: int
    assists: int 
    gold: int
    cs: int
    champion_id: int
    queue_type: str
    role: int
    vision: int

def get_match_history(content):
    return content['data']['fetchPlayerMatchSummaries']['matchSummaries']

def get_player_match_info(m):
    return MatchHistory(
        win = m['win'],
        kills = m['kills'],
        deaths = m['deaths'],
        assists = m['assists'],
        gold = m['gold'],
        cs = m['cs'],
        champion_id = m['championId'],
        queue_type = m['queueType'],
        role = m['role'],
        vision = m['visionScore']
    )

def parse_player_match_history(json_response):
    match_history = get_match_history(json_response)
    return [
        get_player_match_info(m) for m in match_history
    ]

            
def create_player_query_from_template(query_template, player_name, tag_line, page):
    with open(query_template, 'r') as payload:
        data = json.load(payload) 
        data['variables']['riotUserName'] = player_name
        data['variables']['page'] = page
        data['variables']['riotTagLine'] = tag_line
        return data

