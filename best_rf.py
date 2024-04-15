import argparse
from Bio import SeqIO
import utils

ap = argparse.ArgumentParser()
ap.add_argument('-t')
args = vars(ap.parse_args())


sequences = utils.read_fasta_file(args['t'])
longest_sequence_id = max(sequences, key=lambda x: len(sequences[x]))
longest_sequence = sequences[longest_sequence_id]

longest_sequence_dict = {longest_sequence_id: longest_sequence}
utils.write_fasta_file('fasta_longest.fasta', longest_sequence_dict)
