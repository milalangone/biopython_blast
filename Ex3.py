import pandas as pd
import time
import utils
import subprocess

def progresive_alignment(archivo_entrada, archivo_salida = "progresive_output.fasta"):
	command = [
		'clustalo',
		'-i', archivo_entrada,
		'-o', archivo_salida,
		'--outfmt', 'fasta',
		'--force'
	]
	subprocess.run(command, stdout = subprocess.PIPE)

def iterative_alignment(archivo_entrada, archivo_salida = "iterative_output.fasta"):
	command = [
		'muscle',
		'-in',  archivo_entrada,
		'-out', archivo_salida
		]
	subprocess.run(command, stdout=subprocess.PIPE)

def calculate_excecution_time(func):
    start_time = time.time()
    func("sequences_10.fasta")
    end_time = time.time()
    execution_time = end_time - start_time
    return execution_time

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
	
	tiempo_ejecucion_p = calculate_excecution_time(progresive_alignment)
	tiempo_ejecucion_i = calculate_excecution_time(iterative_alignment)

	data = {
	    "Función de Alineamiento": ["Progresivo", "Iterativo"],
	    "Tiempo de Ejecución (s)": [tiempo_ejecucion_p, tiempo_ejecucion_i]
	}

	df = pd.DataFrame(data)
	print("El tiempo de ejecucion de cada algoritmo es:\n", df)
	print('Alineamiento multiple realizado y resultados guardados con exito')
else:
	print("Error: Debes proporcionar al menos un archivo de secuencia query con el argumento -q")


