# TP 1 - Bioinformática

El archivo pipeline.sh permite ejecutar el ejercicio 1 integramente. Se debe contar con un archivo de secuencias llamado "sequence.gb" en el mismo path. (Descargar del notion y no pushear)

## Ejercicio 1

- Ex1.py:

  - Recibe la secuencia de uno o varios transcriptos en un archivo de formato Genbank.
  - Traduce los seis marcos de lectura teniendo en cuenta los codones de inicio y de stop
  
- best_rf.py:

  - Busca la secuencia de aminoàcidos mas larga de todos los transcriptos de todos los marcos de lectura. Asumimos que la cadena mas larga es la mas probable en la naturaleza.
  - input: un unico archivo en formato fasta con varias secuencias de aminoacidos con sus correspondientes ids.
  - output: archivo en formato fasta con la secuencia de aminoacidos mas larga.

## Ejercicio 2

- Ex2.py
  - Toma el archivo fasta de salida y realiza un BLAST a la misma, dejando los resultados en un archivo blast.out
  - input: archivo en formato fasta de la secuencia de AA más larga
  - output: archivo output del BLAST realizado para esta secuencia de AA más larga.
