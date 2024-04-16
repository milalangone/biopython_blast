import utils

ap = utils.argparse.ArgumentParser()
ap.add_argument('-t')
args = vars(ap.parse_args())

if args['t']:

	sequences = utils.read_fasta_file(args['t'])
	longest_sequence_id = max(sequences, key=lambda x: len(sequences[x]))
	longest_sequence = sequences[longest_sequence_id]

	longest_sequence_dict = {longest_sequence_id: longest_sequence}
	utils.write_fasta_file("fasta_longest.fasta", longest_sequence_dict)
	
	print('Se ha encontrado el mejor Reading Frame y los resultados fueron guardados con exito')
else:
	print("Error: Debes proporcionar al menos un archivo de secuencia con el argumento -t")
