#!/usr/bin/env python
import argparse
import json
import sys

def get_bacteria(b):
    orgs = {}
    for i, line in enumerate(b):
        if not len(line.strip()) > 0 or line.startswith('#'):
            continue

        l = line.split('\t')
        if len(l[3].split()) > 1:
            bact_name = l[3].split()[0] + ' ' + l[3].split()[1]
        else:
            bact_name = l[3]

        if bact_name not in orgs:
            orgs[bact_name] = {"group": l[5], "gram": l[9]}
        else:
            g = orgs[bact_name]["gram"]
            if g and l[9] and g is not l[9]:
                print str(i+1) + ": " + bact_name + " gram was " + g + " but another one says " + l[9]
            else:
                orgs[bact_name] = {"group": l[5], "gram": l[9]}

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='parses ncbi bacteria file to get gram information')
    parser.add_argument('b', type=argparse.FileType("r"), help='bacteria txt file')
    args = parser.parse_args()

    get_bacteria(args.b)
