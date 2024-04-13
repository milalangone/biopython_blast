import argparse
from Bio import SeqIO

ap = argparse.ArgumentParser()
ap.add_argument('-t')
args = vars(ap.parse_args())

def write_longest_sequence(filename, sequences):
    longest_sequence_id = max(sequences, key=lambda x: len(sequences[x]))
    longest_sequence = sequences[longest_sequence_id]
    with open(filename, "w") as fasta_file:
        fasta_file.write(f">{longest_sequence_id}\n{longest_sequence}\n")

sequences = read_fasta_file(args['t'])
write_longest_sequence('fasta_longest.fasta',sequences)
