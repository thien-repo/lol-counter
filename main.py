from aggregator import *
import time

def main():
    tags = [
        PlayerTag(name='Reap', tag='na0'),
        PlayerTag(name='YOXEL4796', tag='na1'),
        PlayerTag(name='Glich', tag='SPOIL'),
        PlayerTag(name='bidp', tag='NA2'),
        PlayerTag(name='m8r', tag='troll'),
    ]
    start = time.time()
    with multiprocessing.Pool(len(tags)) as pool:
        results = pool.map(aggregate_worker, tags)
        for i in range(len(tags)):
            print(f'{tags[i].name}#{tags[i].tag}\n\t{results[i]}')
    end = time.time()
    print(end - start)

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
    