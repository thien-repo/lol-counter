from aggregator import *
import time
from tabulate import tabulate
import argparse

import json

def parse_player(pname):
    name, tag = pname.split('#')
    return PlayerTag(name=name, tag=tag)

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--players', type=str, action='append')
args = parser.parse_args()

if args.players == None:
	print('no players added')
	exit(1)

tags = [ parse_player(pname) for pname in args.players ]

def main():
    print('finding players info')
    start = time.time()
    infos = aggregate_players(tags)
    end = time.time()
    print('took',end - start, 'seconds')
    rows = [ normalize(tags[i], infos[i]) for i in range(len(tags)) ]
    table_headers = ['Name', 'Win%', 'Avg Kills', 'Avg Assists', 'Avg CS', 'Avg Vision', 'Avg Gold', 'Most Played Champion', 'Player Type', 'Most Played Role']
    tbl = tabulate(rows,  headers=table_headers, tablefmt='orgtbl')
    print(tbl)
    
        
if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
    
