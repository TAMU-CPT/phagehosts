from Bio import motifs
import argparse
import sys

def parse_meme(meme):
    record = motifs.parse(meme, "meme")
    for motif in record:
        for i in motif.instances:
            print i.sequence_name
        print dir(motif)
        sys.exit()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='clusters meme results')
    parser.add_argument('meme', type=argparse.FileType("r"), help='meme file')
    args = parser.parse_args()

    parse_meme(args.meme)
