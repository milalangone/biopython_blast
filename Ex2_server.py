from Bio.Blast import NCBIWWW
import utils

def run_blast(sequence_data, output_file):
    print("Por empezar a realizar el Blast")
    # Realizar BLAST de la secuencia
    result_handle = NCBIWWW.qblast("blastp", "swissprot", sequence_data, hitlist_size=20)
    print("Blast Finalizado")
    # Guardar el resultado en un archivo
    with open(output_file, "w") as out_handle:
        out_handle.write(result_handle.read())

    result_handle.close()


ap = utils.argparse.ArgumentParser()
ap.add_argument('-f', help='Para ingresar la o las secuencias con mejor Reading Frame en formato Fasta')
args = vars(ap.parse_args())

# Verificar si se proporcionó el argumento '-f'
if args['f']:
    sequences = utils.read_fasta_file(args['f'])
    for key, value in sequences.items():
        output_file = "server_blast.out"

        # Realizar BLAST y guardar el resultado en un archivo
        run_blast(value, output_file)

    print("BLAST completado y resultados guardados.")
    
else:
    print("Error: Debes proporcionar al menos un archivo de secuencia con el argumento '-f'.")


# Ejercicio 2.b - Interpretación del resultado del BLAST.
# Dar una explicación del resultado blast obtenidoen términos de las secuencias enscontradas y dar una explicación 
# sobre que significan los valores estadísticos asociados a las secuencias encontradas (el capítulo 4 del libro de David Mount puedeayudarlos)



