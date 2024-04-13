# Ejercicio 2:
# Ejercicio 2.a - BLAST.
# Escribir un script que realice un BLAST de una o varias secuencias (si son varias se realiza un Blast por cada secuencia input) 
# y escriba el resultado (blast output) en un archivo. 

# Nota: Pueden ejecutar BLAST de manera remota o bien localmente (si hacen ambos tienen más puntos!),para esto deben instalarse0
# BLAST localmente del FTP del NCBI, luego bajarse la base de datos ftp://ftp.ncbi.nlm.nih.gov/blast/db/FASTA/swissprot.gz y descomprimirla en un dir 
# por ej. ncbi-blast2.3.0+/data/, luego usar el # comando ncbi-blast-2.3.0+/bin/makeblastdb sobre el archivoswissprot (el original ya está en formato FASTA) 
# para darle formato de BLAST DB. # Dependiendo de laversión de Blast suite que tengan instalado puede que en vez de makeblastdb deban 
# utilizar elcomando formatdb.
# − Input: Secuencia Fasta (ej. Xxxx.fas con una o más secuencias de aminoácidos obtenidas en Ej.1).
# − Output: Reporte Blast (ej. blast.out, si deciden hacer múltiples pueden generar un único o variosarchivos). 
# Deben entregar el script Ex2.pm y su input file con una breve descripción de lo quehicieron, con una interpretación 
# de los resultados del Blast, y mencionar como se debe ejecutar paraprobarlo.

from Bio import SeqIO
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
import numpy as np

def perform_blast(sequence_file):
    # Aquí deberías tener la lógica para realizar el BLAST con el archivo de secuencias
    # Este es solo un ejemplo de cómo se llamaría al BLAST con Biopython
    result_handle = NCBIWWW.qblast("blastn", "nt", open(sequence_file).read())
    
    # Puedes hacer lo que quieras con el resultado del BLAST aquí
    # Por ahora, simplemente imprimimos los resultados
    print(result_handle.read())

if __name__ == "__main__":
    if "--output-fasta" in sys.argv:
        fasta_file = generate_sequences_fasta()
        print(fasta_file)
    else:
        # Esperamos que el primer argumento sea el archivo FASTA de entrada
        fasta_file = sys.argv[1]
        perform_blast(fasta_file)

# Ejercicio 2.b - Interpretación del resultado del BLAST.
# Dar una explicación del resultado blast obtenidoen términos # de las secuencias enscontradas y dar una explicación 
# sobre que significan los valoresestadísticos asociados a las secuencias encontradas (el capítulo 4 del libro de David Mount puedeayudarlos)



