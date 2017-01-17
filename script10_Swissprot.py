#Imports
import time
from Bio import SeqIO

print "SWISSPROT Entries"
print ""
with open('accessions.txt') as file:
    for line in file:
        line =  line.strip('\n')
        handle = ExPASy.get_sprot_raw(line)
        seq_record = SeqIO.read(handle, "swiss")
        handle.close()
        gene_name = seq_record.annotations['gene_name']
        print "Gene Name: ", gene_name[-8:-1]
        print "Entry Name: ", seq_record.name
        print "Sequence length: ", len(seq_record.seq)
        print "Organism: ", seq_record.annotations['organism']
        print "Organism Classification: ", seq_record.annotations['taxonomy']
        print "Taxonomic ID: ", seq_record.annotations['ncbi_taxid'][0]
        print "Description: ", seq_record.description
        print ""
        time.sleep(1)
