from Bio import SeqIO

def read_genbank_file(filename):
    records = SeqIO.parse(filename, 'genbank')
    sequences = {}
    for record in records:
        sequences[record.id] = str(record.seq)
    return sequences

def write_fasta_file(filename, sequences):
    with open(filename, "w") as fasta_file:
        for key, value in sequences.items():
            for i in range(len(value)):
                SeqIO.write(value[i], fasta_file, "fasta")

def read_fasta_file(file_path):
    sequences = {}
    with open(file_path, "r") as handle:
        for record in SeqIO.parse(handle, "fasta"):
            sequences[record.id] = str(record.seq)
    return sequences