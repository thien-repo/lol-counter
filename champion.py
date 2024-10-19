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

def get_champion_counters_soup(name):
    res = requests.get(f'{config.champion["url"]}/{name}/counter', headers=config.champion['headers'])
    text, status_code = res.text, res.status_code
    if status_code != 200:
        raise Exception(status_code)

    return BeautifulSoup(text, "html.parser")


import config

def main():
    import argparse 
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--champion', type=str)
    args = parser.parse_args()
    name = args.champion
    soup = get_champion_counters_soup(name)
    infos = get_champion_info(soup, name)
    best, worst, gold = infos 
    from tabulate import tabulate
    table_headers = [
        'best against',
        'win%',
        'games',
        'worst against',
        'win%',
        'games',
        'lane counter',
        'gold diff',
        'games'
    ]
    size = len(best)
    rows = [ best[i] + worst[i] + gold[i] for i in range(size) ]
    tbl = tabulate(rows, headers=table_headers, tablefmt='orgtbl')
    print(tbl)

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)