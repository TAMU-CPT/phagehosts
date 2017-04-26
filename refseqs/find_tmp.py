from Bio import SeqIO
import argparse
import sys

def gather_cds_info(qualifiers):
    info = []
    translation = ''
    for q in qualifiers:
        if q == 'note' or q == 'product':
            info.append(qualifiers[q][0])
        if q == 'translation':
            translation = qualifiers[q][0]
    return info, translation


def export_seqs(seq_record):
    for num, feature in enumerate(seq_record.features):
        if feature.type != 'CDS':
            continue
        if 'translation' not in feature.qualifiers:
            continue

        with open('no_tmps.fasta', 'w') as outfile:
            outfile.write('>' + seq_record.id + '_' + feature.qualifiers['protein_id'][0])
            outfile.write('\n')
            outfile.write(feature.qualifiers['translation'][0])
            outfile.write('\n')


def find_tmp(gbk):
    # status = {}
    # with open("myos/myos_assigned.txt", "r") as seq_handle:
        # for line in seq_handle:
            # l = line.strip().split('\t')
            # status[l[1]] = l[2]

    count = 0
    ids = []
    for seq_record in SeqIO.parse(gbk, "genbank"):
        tmp_seq = ''
        tmp_id = ''
        tmp_idx = 0

        tmps_in_genome = []
        for num, feature in enumerate(seq_record.features):
            if feature.type != 'CDS':
                continue
            if 'pseudo' in feature.qualifiers:
                continue

            info, translation = gather_cds_info(feature.qualifiers)

            if len(translation) < 100:
                continue

            # print '>' + seq_record.annotations['organism'].replace(' ', '_') + '_' + feature.qualifiers['protein_id'][0] + '_' + status[seq_record.id]
            # print '>' + seq_record.id + '_' + feature.qualifiers['protein_id'][0]
            # print translation

            tmps_in_feature = []
            for i in info:
                if ('measure' in i.lower() and 'tape' not in i.lower()) or ('length' in i.lower()) or ('tape' in i.lower() and 'pentape' not in i.lower() and 'chaperone' not in i.lower() and 'pre' not in i.lower()):
                # if 'measure' in i.lower() and 'tape' not in i.lower():
                    # tmp_inner.append(i)
                    tmps_in_feature.append(i)
                    tmp_seq = translation
                    tmp_id = feature.qualifiers['protein_id'][0]
                    tmp_idx = num

            if len(tmps_in_feature):
                tmps_in_genome.append(tmps_in_feature)

        if len(tmps_in_genome) == 1:
            if len(tmp_seq) > 100:
                count += 1
                print '>' + seq_record.id + '_' + tmp_id + ' ' + ','.join(tmps_in_genome[0])
                print tmp_seq
    # print count

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='find tape measure proteins')
    parser.add_argument('gbk', type=argparse.FileType("r"), help='multi genbank file')
    args = parser.parse_args()

    find_tmp(args.gbk)
    # export_seqs(ids, args.gbk)
