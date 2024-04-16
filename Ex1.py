from Bio.Seq import Seq
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
import utils

def find_start_codons(sequence, frame):
    start_codon = "ATG"  # El codón de inicio común es "ATG"
    start_codon_indices = []
    
    for i in range(frame, len(sequence) - 2, 3):
        codon = sequence[i:i+3]
        if codon == start_codon:
            start_codon_indices.append(i)
    
    return start_codon_indices


def translate_frames(transcript, seq_id, reading_frames = 3):
    translations = {}
    for frame in range(reading_frames):
        idx = find_start_codons(transcript, frame)
        if idx:
            subtranscript = transcript[idx[0]:]
            aa_seq = subtranscript.translate(to_stop = True)
            translations[seq_id + str(frame)] = aa_seq
        else:
             translations[seq_id + str(frame)] = "None"
    return translations


def reverse_complement(sequence):
    return sequence.reverse_complement()
    
ap = utils.argparse.ArgumentParser()
ap.add_argument('-s')
args = vars(ap.parse_args())

if args['s']:

    genbank_file = args['s']
    sequences = utils.read_genbank_file(genbank_file)
    translations = {}
    for key, value in sequences.items():
        transcript = Seq(value)
        translations.update(translate_frames(transcript, key))
        reversed_transcript = reverse_complement(transcript)
        translations.update(translate_frames(reversed_transcript, '-' + key))

    utils.write_fasta_file("fasta_output.fasta", translations)
    print('Traduccion ejecutada y resultados guardados con exito')

else:
	print("Error: Debes proporcionar al menos un archivo de secuencia con el argumento -f")




