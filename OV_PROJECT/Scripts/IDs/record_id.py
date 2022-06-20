from Bio import SeqIO
file = open('Seqs_and_Computed_Descriptors/Human_proteome_reviewed.fasta','r')
for record in SeqIO.parse(file, "fasta"):#file
    print(record.id)
