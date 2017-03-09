from Bio import Entrez
import json

Entrez.email = "cpt@tamu.edu"
handle = Entrez.esearch(db="genome", term="txid10662[Organism:exp]", retmax=600)  #txid10662[Organism:exp] is entrez query for myoviridae
record = Entrez.read(handle)
idlist = record['IdList']

h = Entrez.esummary(db="genome", id=','.join(idlist))
print json.dumps(Entrez.read(h))
