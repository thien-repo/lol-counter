from aggregator import *
import time
from tabulate import tabulate

tags = [
        PlayerTag(name='Reap', tag='na0'),
        PlayerTag(name='mynameisanumber', tag='na1'),
        PlayerTag(name='steviepoo11', tag='na1'),
    ]


rolemap = {
    '1': 'jungle',
    '2': 'support',
    '3': 'carry',
    '4': 'top',
    '5': 'mid',
    '6': 'fill',
}

def fmt_row(tag, info):
    return [
        f'{tag.name}#{tag.tag}',
        info.win,
        info.kills,
        info.assists,
        info.cs,
        info.vision,
        info.gold,
        info.champ,
        info.player_type,
        rolemap.get(str(info.role), str(info.role))
    ]


def main():
    print('finding players info')
    start = time.time()
    infos = aggregate_players(tags)
    end = time.time()
    print('took',end - start, 'seconds')
    rows = [ fmt_row(tags[i], infos[i]) for i in range(len(tags))]
    table_headers = ['Name', 'Win%', 'Avg Kills', 'Avg Assists', 'Avg CS', 'Avg Vision', 'Avg Gold', 'Most Played Champion', 'Player Type', 'Most Played Role']
    tbl = tabulate(rows,  headers=table_headers, tablefmt='orgtbl')
    print(tbl)
    
        
if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
    
