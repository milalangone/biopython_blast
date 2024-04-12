# Ejercicio 2:
# Ejercicio 2.a - BLAST.
# Escribir un script que realice un BLAST de una o varias secuencias (si son variasse realiza un Blast por cada secuencia input) 
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

def DO_BLAST(sequence_data , output):
    
    # Realizar BLAST de la secuencia
    result_handle = NCBIWWW.qblast("blastn", "nt", sequence_data)

    # Guardar el resultado en un archivo
    with open(output, "w") as out_handle:
        out_handle.write(result_handle.read())

    result_handle.close()

for seq_file, out_file in zip(sequences, output_files):
    # Leer la secuencia del archivo FASTA
    seq_record = SeqIO.read(seq_file, "fasta")

    # Realizar BLAST y guardar el resultado en un archivo
    DO_BLAST(seq_record.seq, out_file)

print("BLAST completado y resultados guardados.")

# Ejercicio 2.b - Interpretación del resultado del BLAST.
# Dar una explicación del resultado blast obtenidoen términos # de las secuencias enscontradas y dar una explicación 
# sobre que significan los valoresestadísticos asociados a las secuencias encontradas (el capítulo 4 del libro de David Mount puedeayudarlos)



