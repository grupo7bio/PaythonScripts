#Imports
from Bio import Entrez
from Bio import Medline

#Email necesario para aceder ao NCBI
Entrez.email = "ferreira.90.ricardo@gmail.com"

#Download da informacao sobre a Legionella pneumophila
handle = Entrez.egquery(term = "Legionella pneumophila")
record = Entrez.read(handle)

#Contabilizar o numero de artigos
for row in record["eGQueryResult"]:
    if row["DbName"] == "pubmed":
        total = row["Count"]

#Procurar as identificacoes dos Artigos da Legionella pneumophila da base de dados PubMed
handle = Entrez.esearch(db = "pubmed", term = "Legionella pneumophila")
record = Entrez.read(handle)
idList = record["IdList"]

#Fazer download e parse dos artigos na base de dados pubmed
handle = Entrez.efetch(db = "pubmed", id=idList, rettype="medline", retmode="text")
records = list(Medline.parse(handle))

#Escrever os Artigos pubmed obtidos para um ficheiro texto
Results = open("Artigos Pubmed.txt", "w")
for record in records:
    title = "Title: " + str(record.get("TI", "?"))
    authors = "\nAuthors: " + str(record.get("AU", "?"))
    source = "\nSource: " + str(record.get("SO", "?"))
    Results.write(title + authors + source + "\n\n")
    #record_results.write(a2)
    #record_results.write(a3)
    #record_results.write("\n\n")

Results.close()
