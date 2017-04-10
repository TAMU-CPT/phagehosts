#!/usr/bin/env python

import argparse
import json


def assign_gram(phage_file, bacteria_file):
    # phages = json.load(phage_file)
    bacts = json.load(bacteria_file)

    additions = {
        'Iodobacteriophage': 'Iodobacter',
        'Enterobacteria': 'Enterobacter',
        'Enterobacterial': 'Enterobacter',
        'Enterobacteriaphage': 'Enterobacter',
        'Lelliottia': 'Enterobacter',
        'Cyanophage': 'Cyanobacteria',
        'Pseudomonad': 'Pseudomonas',
        'Puniceispirillum': 'Proteobacteria',
        'Hamiltonella': 'Enterobacteriaceae',
        'Thalassomonas': 'Proteobacteria',
        'Natrialba': 'Archaea',
        'Archaeal': 'Archaea',
        'Methanobacterium': 'Archaea',
        'Methanothermobacter': 'Archaea',
        'Lactoccocus': 'Lactococcus',
        'Streptomyce': 'Streptomyces',
        'Stx2-converting': 'Escherichia',
        'Stx2': 'Escherichia',
        'T4virus': 'Enterobacter',
        'Vibriophage': 'Vibrio',
    }

    ambiguous = {
        'Bacteriophage': 'Paenibacillus',  # phage Lily
        'Phage': 'Proteobacteria',  # phage phiJL001
        'Podovirus': 'Proteobacteria',  # phage phiJL001
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
    # for p in phages:
    for p in phage_file:
        # host = p['Organism_Name'].split()[0]
        host = p.strip().split()[0]

        if host in bacts:
            pass
        elif host in additions:
            host = additions[host]
        elif host in ambiguous:
            # if 'Lau218' in p['Organism_Name'] or 'Lily' in p['Organism_Name'] or 'phiJL001' in p['Organism_Name'] or 'phiNIH1.1' in p['Organism_Name']:
            if 'Lau218' in p or 'Lily' in p or 'phiJL001' in p or 'phiNIH1.1' in p:
                host = ambiguous[host]
            elif 'APSE-2' in p:  # podophage with host Hamiltonella
            # elif 'APSE-2' in p['Organism_Name']:  # podophage with host Hamiltonella
                host = 'Enterobacteriaceae'
            elif 'vB_EcoP_SU10' in p:  # podophage with host E. coli
            # elif 'vB_EcoP_SU10' in p['Organism_Name']:  # podophage with host E. coli
                host = 'Escherichia'
        else:
            host = 'Unknown'

        # types[bacts[host]] += 1
        # print p['Organism_Name'] + '\t' + bacts[host]
        print p.strip() + '\t' + bacts[host]

    # print types

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='assigns gram to phages')
    parser.add_argument('p', type=argparse.FileType("r"), help='phage file')
    parser.add_argument('b', type=argparse.FileType("r"), help='bacterial host file')
    args = parser.parse_args()

    assign_gram(args.p, args.b)
