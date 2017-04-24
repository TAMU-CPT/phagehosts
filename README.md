# Phage Hosts

Aims:
- make a master bacterial database file that has accurate Gram status information
- isolate refseqs of phages in Myoviridae and Siphoviridae
- determine the bacterial host of each phage and determine the Gram status of each host (using bacterial db)
- isolate annotated tape measure proteins from each phage
- analyze motifs for each annotated tape measure protein (TMP)
- find the TMP in phages with no annotated TMP

## Data flow (so far)
#### Fetch ids for phages
Export list of ids (accession numbers) from NCBI

#### Get genbank files for this list of ids
Use efetch to get genbank files (TODO: comment on this process)

#### Output name, id, and gram status of the host for each phage in the gbk file
```console
$ python assign_phages.py multi_gbk_file.gbk bacterial_host_file.json
```
