import requests
from bs4 import BeautifulSoup
import argparse

def get_champions_from_tag(soup, tag):
    cards = soup.find_all('a', tag)
    return [
        [   
            card.find('div', class_='champion-name').text,
            card.find('div', class_='win-rate').text,
            card.find('div', class_='total-games').text
        ] 
        for card in cards
    ]
    
def get_champion_info(name):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
    }
    url = f'https://u.gg/lol/champions/{name}/counter'
    res = requests.get(url, headers=headers)
    text, status_code = res.text, res.status_code
    if status_code != 200:
        raise Exception(status_code)

    soup = BeautifulSoup(text, "html.parser")
    best = get_champions_from_tag(soup, 'counter-list-card best-win-rate')
    worst = get_champions_from_tag(soup, 'counter-list-card worst-win-rate')
    gold = get_champions_from_tag(soup, 'counter-list-card gold-diff')
    return  best, worst, gold


try:
    best, worst, gold = get_champion_info('akali')
    info = zip(best, worst, gold)
    for best, worst, gold in info:
        print(best, worst, gold)
except Exception as err:
    print(err)

