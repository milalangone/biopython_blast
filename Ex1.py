from Bio.Seq import Seq
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
import argparse

ap = argparse.ArgumentParser()
ap.add_argument('-s')
args = vars(ap.parse_args())

def find_start_codons(sequence, frame):
    start_codon = "ATG"  # El codón de inicio común es "AUG"
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
            seq_record = SeqRecord(aa_seq, id=f"{seq_id}_frame_{frame}")
            translations.append(seq_record)
        else:
            translations.append(SeqRecord(Seq("None"), id=f"{transcript.id}_frame_{frame}"))
    return translations


def reverse_complement(sequence):
    return sequence.reverse_complement()

def write_fasta_file(filename,sequences):
    with open(filename, "w") as fasta_file:
        for key, value in sequences.items():
            for i in range(len(value)):
                SeqIO.write(value[i], fasta_file, "fasta")


genbank_file = args['s']
records = SeqIO.parse(genbank_file, 'genbank')

translations_dict = {}

for record in records:
    seq_id = record.id
    sequence = record.seq
    transcript = Seq(sequence)
    translations = translate_frames(transcript, seq_id)
    reversed_transcript = reverse_complement(transcript)
    translations.extend(translate_frames(reversed_transcript, '-' + seq_id))
    translations_dict[seq_id] = translations
    
write_fasta_file('fasta_output.fasta',translations_dict)


