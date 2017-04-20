from Bio import motifs
import argparse
import sys


def parse_meme(meme_file, fasta_file):
    seq_names = {}
    all_motifs = motifs.parse(meme_file, "meme")
    for motif in all_motifs:
        for i in motif.instances:
            if i.sequence_name.strip() in seq_names:
                seq_names[i.sequence_name.strip()].append(motif.name)
            else:
                seq_names[i.sequence_name.strip()] = [motif.name]

    clusters = {}
    for n in seq_names:
        if str(seq_names[n]) in clusters:
            clusters[str(seq_names[n])].append(n)
        else:
            clusters[str(seq_names[n])] = [n]

    for c in clusters:
        print c, len(clusters[c])


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='clusters meme results')
    parser.add_argument('meme', type=argparse.FileType("r"), help='meme file')
    parser.add_argument('fasta', type=argparse.FileType("r"), help='fasta file')
    args = parser.parse_args()

    parse_meme(args.meme, args.fasta)
