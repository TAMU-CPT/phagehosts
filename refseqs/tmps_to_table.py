from Bio import SeqIO
import argparse
import sys

def output_table(tmps, phages):
    data = {}
    for p in phages:
        info = p.strip().split('\t')
        data[info[1]] = [info[0], info[2]]

    for tmp in SeqIO.parse(tmps, 'fasta'):
        org = tmp.id.rsplit('_', 1)[0].rsplit('_', 1)[0]
        ptn = tmp.id.split('_', 1)[1].split('_', 1)[1]
        data[org].append(ptn)
        data[org].append('\n'.join(['">' + ptn, str(tmp.seq) + '"']))

    for d in sorted(data):
        if len(data[d]) == 4:
            print '\t'.join([data[d][0], d, data[d][1], data[d][2], data[d][3]])
        else:
            print '\t'.join([data[d][0], d, data[d][1]])

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='outputs tmp ids to tabular file with phage names/acessions')
    parser.add_argument('tmps', type=argparse.FileType("r"), help='fasta file of tmps')
    parser.add_argument('phages', type=argparse.FileType("r"), help='tabular file with phage name/accession/gram status')
    args = parser.parse_args()

    output_table(args.tmps, args.phages)
