#Imports
from Bio import SeqIO

#Load GenBank and Fasta Files
ft_record = SeqIO.read("sequence.fasta", "fasta")
gb_record = SeqIO.read("sequence.gb", "genbank")

#Parse the files to extract improtant information
for feature in gb_record.features:
	#if feature.location.start >= 1533851 and feature.location.end <= 1786150:
		if feature.type != 'gene' and feature.type != 'source':
			print("Gene Identification: ")
			print "Type: ", feature.type
			print "GeneID: ", feature.qualifiers['db_xref']
			print "Locus TAG: ", feature.qualifiers['locus_tag']
			if feature.qualifiers.has_key('gene'):
				print "Gene Name: ", feature.qualifiers['gene']
			if hasattr(feature, 'strand'):
				print "Strand: ", feature.strand
				strand = feature.strand
			start = feature.location.start
			end = feature.location.end
			print "Protein Identification:"
			if feature.qualifiers.has_key('protein_id'):
				print "UniprotID: ", feature.qualifiers['protein_id']
			if feature.qualifiers.has_key('product'):
				print "Protein Name: ", feature.qualifiers['product']
			#print('Subsequence:')
			if strand == 1:
				prot_seq = ft_record.seq[start:end]
			else:
				prot_seq = ft_record.seq[start:end]
				prot_seq = prot_seq.reverse_complement()
			#print(prot_seq)
			print "Protein Properties:"
			if feature.qualifiers.has_key('protein_id'):
				#print "Celular Location: ", feature.location
				print "Celular Location Start: ", feature.location.start
				print "Celular Location End: ", feature.location.end
				print "Amino Acids Number: ", len(prot_seq)
			if feature.qualifiers.has_key('EC_number'):
				print "EC Number: ", feature.qualifiers['EC_number']
			if feature.qualifiers.has_key('function'):
				print "Description: ", feature.qualifiers['function']
			print(" ")