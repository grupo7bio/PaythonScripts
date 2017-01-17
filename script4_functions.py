#Imports
from Bio import SeqIO

#Load GenBank File
gb_record = SeqIO.read("sequence.gb", "genbank")

functions = []

for feature in gb_record.features:
    if feature.type == "CDS":
        if 'function' in feature.qualifiers:
            functions.append((feature.qualifiers["locus_tag"][0], feature.qualifiers["function"][0]))

print "FUNCTIONS"
for function in functions:
    print function
