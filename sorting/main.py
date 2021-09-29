from argparse import ArgumentParser
from merge import merge_sort
import random


def parse_args():
    parser = ArgumentParser(description='Sorts numbers')
    parser.add_argument('-method', '-m', type=str, dest='method')
    parser.add_argument('-count', '-n', type=int, dest='n')
    parser.add_argument('-seed', '-s', type=int, dest='seed')
    args = parser.parse_args()
    return args, parser


def main():
    args, parser = parse_args()
    rnd_list = []

    random.seed = args.seed

    for i in range(args.n):
        rnd_list.append(random.randint(0, 10000))

    print(rnd_list)
    output = merge_sort(rnd_list)
    print(output)
    print(sorted(rnd_list) == output)


if __name__ == "__main__":
    main()
