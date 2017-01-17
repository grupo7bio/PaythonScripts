#Imports
from Bio import SeqIO
from Bio.Alphabet import IUPAC
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
from Bio.Blast import NCBIWWW

#Load GenBank File
gb_record = SeqIO.read("sequence.gb", "genbank")

#Create File to store the Blast results
blast_file = open("complete_blast.xml", "w")

#Array Initialize
proteins = []

#find all the CDS features in the files and put them in a List
for feature in gb_record.features:
    if feature.type == "CDS":
        protein = Seq(str(feature.qualifiers['translation']), IUPAC.extended_protein)
        record = SeqRecord(protein)
        proteins.append(record)

#Blast every feature and store all the results into a single file
for protein in proteins:
    blast_result = NCBIWWW.qblast('blastp', 'nr', protein.format('gb'))
    blast_file.write(blast_result.read())

blast_file.close()
blast_result.close()
