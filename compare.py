#!/usr/bin/env python

import argparse
import json


def compare_files(ncbi, labrat):
    bact_ncbi = json.load(ncbi)
    bact_labrat = {}
    for line in labrat:
        l = line.strip().split('\t')
        bact_labrat[l[0]] = l[1]

    a = bact_ncbi.viewkeys() & bact_labrat.viewkeys()  # set of same entry
    b = bact_ncbi.viewkeys() ^ bact_labrat.viewkeys()  # set of unique entries

    for i in sorted(list(a)):
        n = bact_ncbi[i]["gram"]
        l = bact_labrat[i]
        if n == l:
            print i + '\t' + n


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='compares ncbi to thelabrat.com')
    parser.add_argument('ncbi', type=argparse.FileType("r"), help='ncbi file')
    parser.add_argument('labrat', type=argparse.FileType("r"), help='thelabrat.com file')
    args = parser.parse_args()

    compare_files(args.ncbi, args.labrat)
