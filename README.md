# TP 1 - Bioinformática

El archivo **pipeline.sh** permite ejecutar el ejercicio 1, 2 y 3 íntegramente. Se debe contar con un archivo de secuencias llamado "sequence.gb" en el mismo _path_, decidimos no incluirlo en este repositorio, pero puede descargarse en el siguiente [enlace]([enlace](https://drive.google.com/file/d/1kc1isJw3agbjIMkszY0KfMPjylPciBxx/view?usp=sharing)).

## Ejercicio 1

- **Ex1.py**:

  - Recibe la secuencia de uno o varios transcriptos en un archivo de formato Genbank.
  - Traduce los seis marcos de lectura teniendo en cuenta los codones de inicio y de stop
  
- **best_rf.py**:

  - Busca la secuencia de aminoàcidos mas larga de todos los transcriptos de todos los marcos de lectura. Asumimos que la cadena mas larga es la mas probable en la naturaleza.
  - input: un unico archivo en formato fasta con varias secuencias de aminoacidos con sus correspondientes ids.
  - output: archivo en formato fasta con la secuencia de aminoacidos mas larga.

## Ejercicio 2

- **Ex2.py**
  - Toma el archivo fasta de salida y realiza un BLAST a la misma, dejando los resultados en un archivo blast.out
  - input: archivo en formato fasta de la secuencia de AA más larga
  - output: archivo output del BLAST realizado para esta secuencia de AA más larga.
 
## Ejercicio 3

- **Ex3.py**
  - Toma el archivo BLAST de salida y busca los primeros 10 hits. Realiza el alienamiento progresivo e iterativo con las 10 secuencias obtenidas del BLAST y la secuencia _query_.
  - input: archivo en BLAST
  - output: archivos de alineamiento progresivo con CLUSTAW y alineamiento iterativo con MUSCLE.

- **utils.py**
  - Contiene las funciones correspondientes para lectura y escritura de archivos de tipo Genbank, Blast y Fasta. También incluye la importación de la librería _argparse_ que es utilizada a lo largo de todos los _scripts_.
