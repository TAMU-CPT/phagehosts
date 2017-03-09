#!/usr/bin/env python
from Bio import Entrez
import argparse
import json

def get_orgs(tid):
    """ returns a json string of descriptions of all organisms in given taxon """
    Entrez.email = "cpt@tamu.edu"
    handle = Entrez.esearch(db="genome", term="txid%s[Organism:exp]" % tid, retmax=10000)
    record = Entrez.read(handle)
    idlist = record['IdList']

    h = Entrez.esummary(db="genome", id=','.join(idlist))
    return json.dumps(Entrez.read(h))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='outputs json summaries of organisms in a taxon')
    parser.add_argument('tid', type=str, help='taxon id')
    args = parser.parse_args()

    print get_orgs(args.tid)
