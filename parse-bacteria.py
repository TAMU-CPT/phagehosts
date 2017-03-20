#!/usr/bin/env python
import argparse

"""
- Acidobacteria
- Alphaproteobacteria
- Betaproteobacteria
- Gammaproteobacteria
- Deltaproteobacteria
- Epsilonproteobacteria
- Aquificae
- Cyanobacteria
- Spirochaetes
- Thermotogae
- Bacteroidetes/Chlorobi
- Planctomycetes
- Fusobacteria
- Chlamydiae/Verrucomicrobia
- Deinococcus-Thermus  # note: some deinococcus are sudo(?)-positive, but no phages have this host anyway
- Chloroflexi (Sphaerobacter is +)
+ Tenericutes
+/- Actinobacteria
    (mycobacteria are in own category;
     gardnerella are gram variable;
     mobiluncus is - or variable;
     Saccharomonospora viridis is -
     )
+/- Firmicutes
    (Acetivibrio
     Acetohalobium
     Acetonema
     Acholeplasma
     Acidaminococcus
     Anaeroglobus
     Brevibacillus
     Butyrivibrio
     Catonella
     Coprothermobacter
     Dehalobacter
     Dialister
     Faecalibacterium
     Halo
     Helio
     Johnsonella
     Megamonas
     Megasphaera
     Mitsuokella
     Mycoplasma
     Oscillibacter
     Phascolarctobacterium
     Selenomonas
     Subdoligranulum
     Symbiobacterium
     Syntrophobotulus
     Syntrophothermus
     Thermodesulfobium
     Thermosediminibacter
     Thermosinus
     Ureaplasma
     Veillonella)
[ignoring] Other Bacteria

"""

gram_negative = [
    'Acidobacteria',
    'Alphaproteobacteria',
    'Betaproteobacteria',
    'Gammaproteobacteria',
    'Deltaproteobacteria',
    'Epsilonproteobacteria',
    'Aquificae',
    'Cyanobacteria',
    'Spirochaetes',
    'Thermotogae',
    'Bacteroidetes/Chlorobi',
    'Planctomycetes',
    'Fusobacteria',
    'Chlamydiae/Verrucomicrobia',
    'Deinococcus-Thermus',
    'Chloroflexi'
]

negative_exceptions = [
    'Acetivibrio',
    'Acetohalobium',
    'Acetonema',
    'Acholeplasma',
    'Acidaminococcus',
    'Anaeroglobus',
    'Brevibacillus',
    'Butyrivibrio',
    'Catonella',
    'Coprothermobacter',
    'Dehalobacter',
    'Dialister',
    'Faecalibacterium',
    'Halo',
    'Helio',
    'Johnsonella',
    'Megamonas',
    'Megasphaera',
    'Mitsuokella',
    'Mycoplasma',
    'Oscillibacter',
    'Phascolarctobacterium',
    'Selenomonas',
    'Subdoligranulum',
    'Symbiobacterium',
    'Syntrophobotulus',
    'Syntrophothermus',
    'Thermodesulfobium',
    'Thermosediminibacter',
    'Thermosinus',
    'Ureaplasma',
    'Veillonella'
]

def negative_exception(name):
    for i in negative_exceptions:
        if name.startswith(i):
            return True
    return False

def get_bacteria(b):
    orgs = {}
    for i, line in enumerate(b):
        gram = ''

        # ignore blank/comment lines
        if not len(line.strip()) > 0 or line.startswith('#'):
            continue

        l = line.split('\t')

        # ignore irrelevant categories
        if l[4] == 'Archaea' or l[5] == 'Other Bacteria':
            continue

        # get genus and species if possible
        if len(l[3].split()) > 1:
            bact_name = l[3].split()[0] + ' ' + l[3].split()[1]
        else:
            bact_name = l[3].split()[0]

        # assign gram based on phyla
        if bact_name.startswith('Mycobacteria'):
            gram = 'myco'
        elif l[5] in gram_negative or negative_exception(bact_name):
            gram = 'negative'
        else:
            gram = 'positve'

        orgs[bact_name] = {"group": l[5], "gram": gram}

    return orgs

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='parses ncbi bacteria file to get gram information')
    parser.add_argument('b', type=argparse.FileType("r"), help='bacteria txt file')
    args = parser.parse_args()

    bacteria = get_bacteria(args.b)
    for b in sorted(bacteria):
        print b + '\t' + bacteria[b]["gram"]
