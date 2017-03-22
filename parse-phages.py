#!/usr/bin/env python

import argparse
import json


def get_phages(p):
    count = 0
    for line in p:
        if line.strip() and line.strip().split()[0].strip('.').isdigit():
            if "UNVERIFIED" in line:
                continue
            if "partial genome" in line or "partial sequence" in line:
                print line.strip()
                continue
            if "complete genome" not in line and "complete sequence" not in line:
                print line.strip()
                continue
            count += 1
    print count

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='parses ncbi phage file to get get phage names')
    parser.add_argument('p', type=argparse.FileType("r"), help='phage file')
    args = parser.parse_args()

    get_phages(args.p)
