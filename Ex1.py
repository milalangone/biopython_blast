from Bio.Seq import Seq
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
import argparse
import utils

ap = argparse.ArgumentParser()
ap.add_argument('-s')
args = vars(ap.parse_args())

def find_start_codons(sequence, frame):
    start_codon = "ATG"  # El codón de inicio común es "ATG"
    start_codon_indices = []
    
    for i in range(frame, len(sequence) - 2, 3):
        codon = sequence[i:i+3]
        if codon == start_codon:
            start_codon_indices.append(i)
    
    return start_codon_indices


def translate_frames(transcript, seq_id, reading_frames = 3):
    translations = []
    for frame in range(reading_frames):
        idx = find_start_codons(transcript, frame)
        if idx:
            subtranscript = transcript[idx[0]:]
            aa_seq = subtranscript.translate(to_stop = True)
            seq_record = SeqRecord(Seq(aa_seq), id=f"{seq_id}_frame_{frame}")
            translations.append(seq_record)
        else:
            translations.append(SeqRecord(Seq("None"), id=f"{transcript.id}_frame_{frame}"))
    return translations


def reverse_complement(sequence):
    return sequence.reverse_complement()


genbank_file = args['s']

sequences = utils.read_genbank_file(genbank_file)
translations_dict = {}

for key, value in sequences.items():
    transcript = Seq(value)
    translations = translate_frames(transcript, key)
    reversed_transcript = reverse_complement(transcript)
    translations.extend(translate_frames(reversed_transcript, '-' + key))
    translations_dict[key] = translations

    
utils.write_fasta_file("fasta_output.fasta", translations_dict)


