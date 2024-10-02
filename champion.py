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
    
def get_champion_info(soup, name):
    best = get_champions_from_tag(soup, 'counter-list-card best-win-rate')
    worst = get_champions_from_tag(soup, 'counter-list-card worst-win-rate')
    gold = get_champions_from_tag(soup, 'counter-list-card gold-diff')
    return  best, worst, gold

def get_champion_counters_soup(url, headers):
    res = requests.get(f'{url}/{name}/counter', headers=headers)
    text, status_code = res.text, res.status_code
    if status_code != 200:
        raise Exception(status_code)

    return BeautifulSoup(text, "html.parser")

