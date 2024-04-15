from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

def read_genbank_file(filename):
    records = SeqIO.parse(filename, 'genbank')
    sequences = {}
    for record in records:
        sequences[record.id] = str(record.seq)
    return sequences

def write_fasta_file(filename, sequences):
    with open(filename, "w") as fasta_file:
        for key, value in sequences.items():
        	SeqIO.write(value, fasta_file, 'fasta')

def read_fasta_file(filename):
    sequences = {}
    for record in SeqIO.parse(filename, 'fasta'):
    	sequences[record.id] = str(record.seq)
    return sequences
