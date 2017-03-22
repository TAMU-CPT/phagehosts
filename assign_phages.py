#!/usr/bin/env python

import argparse
import json


def assign_gram(phage_file, bacteria_file):
    phages = json.load(phage_file)
    bacts = json.load(bacteria_file)

    additions = {
        'Iodobacteriophage': 'Iodobacter',
        'Enterobacteria': 'Enterobacter',
        'Enterobacterial': 'Enterobacter',
        'Enterobacteriaphage': 'Enterobacter',
        'Cyanophage': 'Cyanobacteria',
        'Natrialba': 'Archaea',
        'Archaeal': 'Archaea',
        'Methanobacterium': 'Archaea',
        'Methanothermobacter': 'Archaea',
        'Streptomyce': 'Streptomyces',
        'Stx2-converting': 'Escherichia',
        'T4virus': 'Enterobacter',
    }

    ambiguous = {
        'Bacteriophage': 'Paenibacillus',  # phage Lily
        'Phage': 'Proteus',  # phage phiJL001
        'Temperate': 'Streptococcus',  # phage phiNIH1.1
    }

    types = {
        'negative': 0,
        'positive': 0,
        'myco': 0,
        'unknown': 0,
        'archaea': 0
    }

    hosts = {}
    for p in phages:
        host = p['Organism_Name'].split()[0]

        if host in bacts:
            pass
        elif host in additions:
            host = additions[host]
        elif host in ambiguous:
            if 'Lily' in p['Organism_Name'] or 'phiJL001' in p['Organism_Name'] or 'phiNIH1.1' in p['Organism_Name']:
                host = ambiguous[host]
        else:
            host = 'Unknown'

        types[bacts[host]] += 1
        # print p['Organism_Name'] + '\t' + bacts[host]

    print types

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='assigns gram to phages')
    parser.add_argument('p', type=argparse.FileType("r"), help='phage file')
    parser.add_argument('b', type=argparse.FileType("r"), help='bacterial host file')
    args = parser.parse_args()

    assign_gram(args.p, args.b)
