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

    bact_list = {}

    for i in list(a):
        n = bact_ncbi[i]["gram"]
        l = bact_labrat[i]
        if n == l:
            bact_list[i] = n
            # print i + '\t' + n

    for i in list(b):
        gram = ''
        if i in bact_ncbi:
            gram = bact_ncbi[i]["gram"]
        elif i in bact_labrat:
            gram = bact_labrat[i]

        bact_list[i] = gram

    final_hosts = {}
    for b in sorted(bact_list):
        name = b.strip().split()[0]
        if bact_list[b] != 'unknown':
            if name not in final_hosts:
                final_hosts[name] = bact_list[b]
            else:
                if final_hosts[name] != bact_list[b]:
                    print '****'
                    print b
                    print final_hosts[name], bact_list[b]
                    print '****'

    with open('curated.json', 'w') as final:
        final.write(json.dumps(final_hosts, indent=4, sort_keys=True))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='compares ncbi to thelabrat.com')
    parser.add_argument('ncbi', type=argparse.FileType("r"), help='ncbi file')
    parser.add_argument('labrat', type=argparse.FileType("r"), help='thelabrat.com file')
    args = parser.parse_args()

    compare_files(args.ncbi, args.labrat)
