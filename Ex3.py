from Bio import SeqIO
from Bio import AlignIO
import pandas as pd
import time
import utils
import subprocess

def progresive_alignment(archivo_entrada, archivo_salida = "progresive_output.fasta"):
    from Bio.Align.Applications import ClustalOmegaCommandline
    clustalomega_cline = ClustalOmegaCommandline(infile=archivo_entrada, outfile=archivo_salida, verbose=True, dealign = True)
    stdout, stderr = clustalomega_cline()
    return stdout, stderr


def star_center_alignment(archivo_entrada, archivo_salida = "star_center_output.fasta"):
    from Bio.Align.Applications import TCoffeeCommandline
    tcoffee_cline = TCoffeeCommandline(infile=archivo_entrada, output=archivo_salida)
    stdout, stderr = tcoffee_cline()
    return stdout, stderr


def iterative_alignment(archivo_entrada, archivo_salida = "iterative_output.fasta"):
    from Bio.Align.Applications import MuscleCommandline
    mafft_cline = MuscleCommandline(input=archivo_entrada, out=archivo_salida)
    stdout, stderr = mafft_cline()
    return stdout, stderr

def calculate_excecution_time(func):
    start_time = time.time()
    _, stderr = func("sequences_10.fasta")
    end_time = time.time()
    execution_time = end_time - start_time
    return stderr, execution_time

query = utils.read_fasta_file("fasta_longest.fasta")
blast_records = utils.read_blast("NM_024110.40_blast.out")

sequences_10 = {}
sequences_count = 0 

for blast_record in blast_records:
    for hit in blast_record.hits:
        for hsp in hit.hsps:
            if sequences_count < 10: 
                sequences_10[hsp.hit.id] = hsp.hit.seq
                sequences_count += 1
            else:
                break 
    if sequences_count >= 10:
        break 

sequences_10.update(query)
utils.write_fasta_file("sequences_10.fasta",sequences_10)

stderr_p, tiempo_ejecucion_p = calculate_excecution_time(progresive_alignment)
print("Error progresivo: ", stderr_p)
stderr_i, tiempo_ejecucion_i = calculate_excecution_time(iterative_alignment)
#stderr_s, tiempo_ejecucion_s = calculate_excecution_time(star_center_alignment)

data = {
    "Función de Alineamiento": ["Progresivo", "Iterativo"],
    "Tiempo de Ejecución (s)": [tiempo_ejecucion_p, tiempo_ejecucion_i]
}

df = pd.DataFrame(data)
print(df)


