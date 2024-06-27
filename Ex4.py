import urllib.request
import os
import subprocess
import utils
import argparse
from Bio import SeqIO

ap = utils.argparse.ArgumentParser()
ap.add_argument('-i', '--input', help="Archivo de secuencia de nucleótidos para buscar los ORFs")
ap.add_argument('-s', '--sequence', help="Secuencia de AA para buscar motifs")
args = vars(ap.parse_args())
output_file = 'found_domains.patmatmotifs'

if args['input']:
    orf_output_file = "orfs.fasta"
    getorf_cmd = ['getorf', '-sequence', args['input'], '-outseq', orf_output_file]
    result = subprocess.run(getorf_cmd, stderr=subprocess.PIPE)

    if result.returncode == 0:
        print(f"ORFs calculados y guardados en {orf_output_file}")
    else:
        print("Se produjo un error al calcular los ORFs. Detalle del error: ")
        print(result.stderr.decode())
        exit()


    patmotif_cmd = f'patmatmotifs -sequence {args["sequence"]} -outfile {output_file}'
    print(f'patmotif_cmd es {patmotif_cmd}')
    with open(output_file, "w") as file:
        result = subprocess.run(patmotif_cmd, shell=True, stderr=subprocess.PIPE, stdout=file)
    if result.returncode == 0:
        print(f'Analisis de dominios completado. Se guardaron en el archivo {output_file}')
    else:
        print("Se produjo un error al analizar los dominios. Detalle del error: ")
        print(result.stderr.decode())