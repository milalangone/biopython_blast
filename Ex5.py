from Bio.Seq import Seq
from Bio.SeqUtils import MeltingTemp as mt
from Bio.SeqUtils import gc_fraction
import utils

def valid_gc_content(sequence, min_gc_content,max_gc_content):
    return min_gc_content <= gc_fraction(sequence)*100 <= max_gc_content
    
def valid_lenght(sequence, min_lenght, max_lenght):
    return min_lenght <= len(sequence) <= max_lenght
    
def valid_tm(sequence, max_tm):
    return mt.Tm_NN(sequence) <= max_tm

def has_gc_terminal(sequence):
    return sequence.startswith('G') or sequence.startswith('C') or sequence.endswith('G') or sequence.endswith('C')

def validate_primer(sequence):
    if not valid_lenght(sequence, primer_parameters["min_lenght"], primer_parameters["max_lenght"]) and valid_gc_content(sequence, primer_parameters["min_gc_content"], primer_parameters["max_gc_content"]) and valid_tm(sequence,primer_parameters["max_tm"]):
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

def design_primers(transcript):
    forward_primers = generate_primers(transcript)
    reverse_primers = generate_primers(str(Seq(transcript).reverse_complement()))

    primer_pairs = []
    for fwd in forward_primers:
        for rev in reverse_primers:
            if len(primer_pairs) < int(primer_parameters["min_length"]/2):
                primer_pairs.append([fwd, rev])
            else:
                break
        if len(primer_pairs) >= int(primer_parameters["min_length"]/2):
            break

    return primer_pairs

ap = utils.argparse.ArgumentParser()
ap.add_argument('-s')
ap.add_argument('-j')
args = vars(ap.parse_args())

if args['s'] and args['j']:
    sequences = utils.read_genbank_file(args['s'])
    primer_parameters = utils.read_json(args['j'])
    for transcript in sequences.items():
        primers = design_primers(transcript)