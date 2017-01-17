#Imports
from Bio import SeqIO
from Bio.Alphabet import IUPAC
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
from Bio.Blast import NCBIWWW

#Load GenBank File
gb_record = SeqIO.read("sequence.gb", "genbank")

#Create File to store the Blast results
blast_file = open("single_blast.xml", "w")

#Array Initialize
proteins = []

#find all the CDS features in the files and put them in a List
for feature in gb_record.features:
    if feature.type == "CDS":
        protein = feature.qualifiers['translation'][0]
        proteins.append(protein)

i = 0

#wait for user input to get the position to be Blasted
print "Enter the Position of a singles CDS to obtain it's Blast:",
position = raw_input()

#search for the position entered by the user in the List of CDS features + blast and save the result
for protein in proteins:
    i = i+1
    if str(i) == position:
        blast_result = NCBIWWW.qblast('blastp', 'nr', protein)
        blast_file.write(blast_result.read())

blast_file.close()
blast_result.close()
