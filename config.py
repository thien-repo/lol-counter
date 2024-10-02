player = dict(
    templates_query = 'templates/player_query.json',
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
        "Content-Type": "application/json"
    },
    url = 'https://u.gg/api',
)

champion = dict(
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
    },
    url = 'https://u.gg/lol/champions'
)


# import requests
# import json
# from bs4 import BeautifulSoup
# url = "https://u.gg/api"
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
#     "Content-Type": "application/json"
# }

# with open('query.json', 'r') as payload:
#     data = json.load(payload)
#     res = requests.post(url, headers=headers,json=data)
#     if res.status_code == 200:
#         match_history = get_match_history(json.loads(res.text))
#         for m in match_history:
#             win, kda, vs, gold, cs, champid, qtype = get_player_match_info(m)
#             print(win, kda, vs, gold, cs, champid, qtype)