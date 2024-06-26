from Bio.Seq import Seq
from Bio.SeqUtils import MeltingTemp as mt
from Bio.SeqUtils import gc_fraction
import utils

def valid_gc_content(sequence, min_gc_content,max_gc_content):
    return min_gc_content <= gc_fraction(sequence)*100 <= max_gc_content
    
def valid_length(sequence, min_length, max_length):
    return min_length <= len(sequence) <= max_length
    
def valid_tm(sequence, max_tm):
    return mt.Tm_NN(sequence) <= max_tm

def has_gc_terminal(sequence):
    return sequence.startswith('G') or sequence.startswith('C') or sequence.endswith('G') or sequence.endswith('C')

def validate_primer(sequence):
    if not valid_length(sequence, primer_parameters["min_length"], primer_parameters["max_length"]) or not valid_gc_content(sequence, primer_parameters["min_gc_content"], primer_parameters["max_gc_content"]) or not valid_tm(sequence,primer_parameters["max_tm"]):
        return False
    
    if primer_parameters["allow_gc_terminal"]:
        return True
    return not has_gc_terminal(sequence)


def generate_primers(sequence):
    primers = []
    len_seq = len(sequence)
    for i in range(len_seq - primer_parameters["min_length"]-1): 
        for j in range(primer_parameters["min_length"], primer_parameters["max_length"]+1): 
            primer_seq = sequence[i:i+j]
            if validate_primer(primer_seq):
                primers.append(primer_seq)
                if len(primers) >= primer_parameters["num_primers"]:  
                    break
        if len(primers) >= primer_parameters["num_primers"]:
            break
    return primers

ap = utils.argparse.ArgumentParser()
ap.add_argument('-s')
ap.add_argument('-j')
args = vars(ap.parse_args())

if args['s'] and args['j']:
    sequences = utils.read_genbank_file(args['s'])
    primer_parameters = utils.read_json(args['j'])
    primers = {}
    for key, transcript in (sequences.items()):
        forward_primers = generate_primers(transcript)
        reverse_primers = generate_primers(Seq(str(transcript)).reverse_complement())
        for (i, primer) in enumerate(forward_primers):
            primers[key+f'_fwd_primer_{i}'] = forward_primers[i]
        for (j,r_primer) in enumerate(reverse_primers):
            primers[key+f'_rev_primer_{j}'] = reverse_primers[i]
    utils.write_fasta_file("fasta_primers.fasta", primers)
    print('Primers generados y resultados guardados con exito')

else:
	print("Error: Debes proporcionar al menos un archivo de secuencia con el argumento -s y un archivo JSON con los parametros con el argumento -j")
