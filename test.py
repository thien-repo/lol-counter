import player 
import config

player_name = 'reap'
tag_line = 'na0'
page = 1
query_data = player.create_player_query_from_template( config.player['templates_query'], player_name, tag_line, page )

import requests 

url = 'https://u.gg/lol/profile/na1/sumac-spice/overview'

import json

with open('templates/player_live_game.json', 'r') as file:
    data = json.load(file)
    res = requests.post(
            config.player['url'],
            headers=config.player['headers'],
            json=data
        )
    
    print(res.text)
    # with open('p.json', 'w') as wfile:
    #    wfile.write(res.text)