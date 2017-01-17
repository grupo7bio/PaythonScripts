#Imports
from Bio import SeqIO

#Load GenBank File
gb_record = SeqIO.read("sequence.gb", "genbank")

translations = []

for feature in gb_record.features:
    if feature.type == "CDS":
        translations.append((feature.qualifiers["locus_tag"][0], feature.qualifiers["translation"][0]))


print "TRANSLATIONS"
for translation in translations:
    print translation
