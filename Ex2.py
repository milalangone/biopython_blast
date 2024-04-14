# Ejercicio 2:
# Ejercicio 2.a - BLAST.
# Escribir un script que realice un BLAST de una o varias secuencias (si son varias se realiza un Blast por cada secuencia input) 
# y escriba el resultado (blast output) en un archivo. 
# − Input: Secuencia Fasta (ej. Xxxx.fas con una o más secuencias de aminoácidos obtenidas en Ej.1).
# − Output: Reporte Blast (ej. blast.out, si deciden hacer múltiples pueden generar un único o varios archivos). 
# Deben entregar el script Ex2.pm y su input file con una breve descripción de lo que hicieron, con una interpretación 
# de los resultados del Blast, y mencionar como se debe ejecutar para probarlo.

from Bio import SeqIO
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
import argparse

def do_blast(sequence_data, output_file):
    # Realizar BLAST de la secuencia
    result_handle = NCBIWWW.qblast("blastp", "nr", sequence_data)

    # Guardar el resultado en un archivo
    with open(output_file, "w") as out_handle:
        out_handle.write(result_handle.read())

    result_handle.close()

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument('-f', help='Para ingresar la o las secuencias con mejor Reading Frame en formato Fasta')
    args = vars(ap.parse_args())

    # Verificar si se proporcionó el argumento '-f'
    if args['f']:
        # Lista de secuencias de entrada
        sequence_files = args['f'].split(',')  # Permitir múltiples archivos separados por comas
        
        for seq_file in sequence_files:
            # Leer la secuencia del archivo FASTA
            seq_record = SeqIO.read(seq_file, "fasta")

            # Definir el nombre del archivo de salida
            output_file = seq_file.split('.')[0] + "_blast.out"

            # Realizar BLAST y guardar el resultado en un archivo
            do_blast(seq_record.seq, output_file)

        print("BLAST completado y resultados guardados.")
    else:
        print("Error: Debes proporcionar al menos un archivo de secuencia con el argumento '-f'.")


# Ejercicio 2.b - Interpretación del resultado del BLAST.
# Dar una explicación del resultado blast obtenidoen términos de las secuencias enscontradas y dar una explicación 
# sobre que significan los valores estadísticos asociados a las secuencias encontradas (el capítulo 4 del libro de David Mount puedeayudarlos)



