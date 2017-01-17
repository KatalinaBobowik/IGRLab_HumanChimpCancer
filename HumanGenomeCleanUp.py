#17.01.17

from Bio import SeqIO

#hg38.fa.gz downloaded from UCSC
fasta_file = "/home/users/ntu/kbobowik/genomes/hg38.fa"
wanted_file = "/home/users/ntu/kbobowik/genomes/wanted_file_human.txt"
#empty file to be populated with new, cleaned genome
result_file = "/home/users/ntu/kbobowik/genomes/hg38_clean.fasta"

wanted = set()
with open(wanted_file) as f:
    for line in f:
        line = line.strip()
        if line != "":
            wanted.add(line)

fasta_sequences = SeqIO.parse(open(fasta_file),'fasta')
with open(result_file, "w") as f:
    for seq in fasta_sequences:
        if seq.id in wanted:
            SeqIO.write([seq], f, "fasta")
