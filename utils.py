import json
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
import argparse

def read_genbank_file(filename):
    records = SeqIO.parse(filename, 'genbank')
    sequences = {}
    for record in records:
        sequences[record.id] = str(record.seq)
    return sequences

def write_fasta_file(filename, sequences):
    with open(filename, "w") as fasta_file:
        for key, value in sequences.items():
            SeqIO.write(SeqRecord(Seq(value), id = key), fasta_file, 'fasta')

def read_fasta_file(filename):
    sequences = {}
    for record in SeqIO.parse(filename, 'fasta'):
         sequences[record.id] = str(record.seq)
    return sequences

def read_blast(filename):
    from Bio import SearchIO
    blast_records = SearchIO.parse(filename, "blast-xml")
    return blast_records

def read_json(filename):
    with open(filename, 'r') as file:
        primer_parameters = json.load(filename)
    return primer_parameters
