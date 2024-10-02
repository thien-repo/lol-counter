from dataclasses import dataclass
import config
import json
import requests
import player
from collections import Counter

def aggregate_match_history(player_name, num_pages):
    match_histories = []
    for page in range(1, num_pages + 1):
        query_data = player.create_player_query_from_template( config.player['templates_query'], player_name, page )
        res = requests.post(
            config.player['url'],
            headers=config.player['headers'],
            json=query_data
        )
        if res.status_code != 200:
            raise Exception(f'{player_name} page {page} failed')
        
        match_history = player.parse_player_match_history(json.loads(res.text))
        for m in match_history:
            match_histories.append(m)

    return match_histories


@dataclass
class SOA:
    win: list
    kills: list
    deaths: list
    assists: list 
    gold: list
    cs: list
    champion_id: list
    queue_type: list
    size: int

def aos_to_soa_match_histories(match_histories):
    return SOA(
        win = [m.win for m in match_histories],
        kills = [m.kills for m in match_histories],
        deaths = [m.deaths for m in match_histories],
        assists = [m.assists for m in match_histories],
        gold = [m.gold for m in match_histories],
        cs = [m.cs for m in match_histories],
        champion_id = [m.champion_id for m in match_histories],
        queue_type = [m.queue_type for m in match_histories],
        size = len(match_histories)
    )

def calculate_player_stats(soa):
    win_percent = sum( soa.win ) / soa.size
    avg_kills = sum(soa.kills) / soa.size 
    avg_deaths = sum(soa.deaths) / soa.size 
    avg_assists = sum(soa.assists) / soa.size 
    avg_cs = sum(soa.cs) / soa.size 
    avg_gold = sum(soa.gold) / soa.size
    most_played_champ = max(set(soa.champion_id),  key=soa.champion_id.count)
    player_type = max(set(soa.queue_type), key=soa.queue_type.count)

    return win_percent, avg_kills, avg_deaths, avg_assists, avg_cs, avg_gold, most_played_champ, player_type

match_histories = aggregate_match_history('reap', 5)

soa = aos_to_soa_match_histories(match_histories)

print(calculate_player_stats(soa))