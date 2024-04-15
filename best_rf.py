import argparse
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
import utils
from Bio.Seq import Seq

ap = argparse.ArgumentParser()
ap.add_argument('-t')
args = vars(ap.parse_args())


sequences = utils.read_fasta_file(args['t'])
longest_sequence_id = max(sequences, key=lambda x: len(sequences[x]))
longest_sequence = sequences[longest_sequence_id]

longest_sequence_dict = {longest_sequence_id: SeqIO.SeqRecord(Seq(longest_sequence), id=longest_sequence_id)}
utils.write_fasta_file("fasta_longest.fasta", longest_sequence_dict)
