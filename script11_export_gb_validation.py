#Imports
from Bio import Entrez
from Bio import SeqIO

#Email necesario para aceder ao NCBI
Entrez.email = "ferreira.90.ricardo@gmail.com"

#Download do ficheiro FASTA correspondente a sequencia desejada
handle=Entrez.efetch(db='nucleotide',id='52840256',rettype='fasta', retmode="fasta")

# Guardar o contiudo num ficheiro FASTA em local
local_file=open('sequence.fasta', 'w')
local_file.write(handle.read())
handle.close()
local_file.close()


#Download do ficheiro GenBank correspondente a sequencia desejada
handle = Entrez.efetch(db="nucleotide", rettype="gb", retmode="text",id="52840256", seq_start="1533851", seq_stop="1786150")
#handle = Entrez.efetch(db="nucleotide", rettype="gb", retmode="text",id="52840256")
seq_record = SeqIO.read(handle, "gb")

# Guardar o contiudo num ficheiro GB em local
SeqIO.write(seq_record, 'sequence.gb', "genbank")
handle.close()

#Imprimir Dados Relevantes na Consola correspondentes ao Ficheiro GenBank
record = SeqIO.read("sequence.gb", "genbank")
print "REGISTO NCBI" + "\n"
print record


#Load GenBank
gb_record = SeqIO.read("sequence.gb", "genbank")

#Load NCBI table refering to the specific Genome Zone
file = open("ProteinTable.txt")
protein_table = []
for line in file.readlines():
    protein_table.append(line.split('\t'))
file.close()

#Retrieve GeneID and ProteinID to compare with the previous table
CDS_ProteinID = []
CDS_GeneID = []

for feature in gb_record.features:
    if feature.type != 'gene' and feature.type != 'source':
        if feature.qualifiers.has_key('protein_id'):
            CDS_ProteinID.append(feature.qualifiers["protein_id"][0])
            CDS_GeneID.append(feature.qualifiers["db_xref"][0].strip("GeneID:"))

#Result validation
valido = True
for j in xrange(0, len(protein_table)):
    if protein_table[j][0].strip() != CDS_GeneID[j] or protein_table[j][1].strip() != CDS_ProteinID[j]:
        valido = False
        print "Feature Error", CDS_GeneID[j], CDS_ProteinID[j]
        print "Table", protein_table[j][0].strip(), protein_table[j][1].strip()

if valido:
    print "A validacao das Features foi efetuada com sucesso!"
else:
    print "Existem Features invalidas!"
