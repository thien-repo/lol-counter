import json

player = dict(
    templates_query = 'templates/player_query.json',
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
        "Content-Type": "application/json"
    },
    url = 'https://u.gg/api',
)

def load_champion_map(fname):
    with open(fname, 'r') as file:
        data = json.loads(file.readline())
        return data

champion_map = load_champion_map('templates/champions.json')

rolemap = {
    '1': 'jungle',
    '2': 'support',
    '3': 'carry',
    '4': 'top',
    '5': 'mid',
    '6': 'fill',
}


champion = dict(
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
    },
    url = 'https://u.gg/lol/champions',
)



