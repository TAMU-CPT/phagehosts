#!/usr/bin/env python

import argparse
import json


def tableify(bacteria_file):
    bacts = json.load(bacteria_file)

    for b in bacts:
        print b + '\t' + bacts[b]
        # cols = []
        # cols.append(b)
        # for i in bacts[b]:
            # cols.append(bacts[b][i])
        # print '\t'.join(cols)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='ncbi bacts to table')
    parser.add_argument('b', type=argparse.FileType("r"), help='ncbi bacts file')
    args = parser.parse_args()

    tableify(args.b)
