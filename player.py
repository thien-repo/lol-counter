import requests
import json
from bs4 import BeautifulSoup
from dataclasses import dataclass

@dataclass
class MatchInfo:
    win: bool 
    kda: list[int]
    vision: int
    gold: int
    cs: int
    champion_id: int 
    queue_type: str



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


def parse_player_match_history(json_response, player_name):
    match_history = get_match_history(json_response)
    return [
        get_player_match_info(m) for m in match_history
    ]

            
def create_player_query_from_template(query_template, player_name, page):
    with open(query_template, 'r') as payload:
        data = json.load(payload) 
        data['riotUserName'] = player_name
        data['page'] = page
        return data

