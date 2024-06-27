import pandas as pd
import time
import utils

def progresive_alignment(archivo_entrada, archivo_salida = "progresive_output.fasta"):
	from Bio.Align.Applications import ClustalOmegaCommandline
	clustalomega_cline = ClustalOmegaCommandline(infile=archivo_entrada, outfile=archivo_salida, force = True)
	stdout, _ = clustalomega_cline()
	return stdout

def iterative_alignment(archivo_entrada, archivo_salida = "iterative_output.fasta"):
    from Bio.Align.Applications import MuscleCommandline
    mafft_cline = MuscleCommandline(input=archivo_entrada, out=archivo_salida)
    stdout, _ = mafft_cline()
    return stdout

def calculate_excecution_time(func):
    start_time = time.time()
    stdout = func("sequences_10.fasta")
    end_time = time.time()
    execution_time = end_time - start_time
    return stdout, execution_time

def best_10_hits(blast_records):

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


ap = utils.argparse.ArgumentParser()
ap.add_argument('-q')
args = vars(ap.parse_args())

if args['q']:
	query = utils.read_fasta_file(args['q'])
	blast_records = utils.read_blast("local_blast_result.out")
	best_10_hits(blast_records)
	
	stdout_p, tiempo_ejecucion_p = calculate_excecution_time(progresive_alignment)
	stdout_i, tiempo_ejecucion_i = calculate_excecution_time(iterative_alignment)

	data = {
	    "Función de Alineamiento": ["Progresivo", "Iterativo"],
	    "Tiempo de Ejecución (s)": [tiempo_ejecucion_p, tiempo_ejecucion_i]
	}

	df = pd.DataFrame(data)
	print("El tiempo de ejecucion de cada algoritmo es:\n", df)
	print('Alineamiento multiple realizado y resultados guardados con exito')
else:
	print("Error: Debes proporcionar al menos un archivo de secuencia query con el argumento -q")


