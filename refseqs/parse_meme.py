from Bio import motifs
import argparse
import sys
import json
from subprocess import call


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

    renumbered = {}
    with open("../seqs.json", 'r') as handle:
        data = json.load(handle)
        seqs = data["sequence_db"]["sequences"]
        for num, seq in enumerate(seqs, 1):
            renumbered[seq["name"]] = num

    for num, c in enumerate(clusters, 1):
        folder = "cluster_%s" % num
        call(["mkdir", folder])
        print '*****'
        print "cluster", num
        print c
        for i in clusters[c]:
            for r in renumbered:
                if str(r).startswith(i):
                    pic_file = str(renumbered[r]) + '.png'
                    call(["cp", pic_file, folder])
                    print renumbered[r], i
        call(["convert", "-append", folder + '/*.png', 'spacer.png', folder + '/out.png'])
        call(["cp", folder + '/out.png', folder + '.png'])
        print '#######'


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='clusters meme results')
    parser.add_argument('meme', type=argparse.FileType("r"), help='meme file')
    parser.add_argument('fasta', type=argparse.FileType("r"), help='fasta file')
    args = parser.parse_args()

    parse_meme(args.meme, args.fasta)
