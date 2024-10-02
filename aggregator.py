from dataclasses import dataclass
import config
import json
import requests
import player


query_data = player.create_player_query_from_template( config.player['templates_query'], 'reap', 1 )


res = requests.post(
    config.player['url'],
    headers=config.player['headers'],
    json=query_data
)


match_history = player.parse_player_match_history(json.loads(res.text))

for m in match_history:
    print(m)