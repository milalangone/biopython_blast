# TP 1 - Bioinformática

El archivo **pipeline.sh** es un script de Bash que permite ejecutar los ejercicio 1, 2 y 3 íntegramente. Todos los ejercicios fueron resueltos utilizando Python, en particular la librería Biopython. Se debe contar con un archivo de secuencias llamado "sequence.gb" en el mismo _path_, decidimos no incluirlo en este repositorio, pero puede descargarse en el siguiente [enlace](https://drive.google.com/file/d/1kc1isJw3agbjIMkszY0KfMPjylPciBxx/view?usp=sharing).

El archivo **prep_env.sh** es el primer paso del pipeline de trabajo e instala el _software_ y dependencias necesarias para la ejecución del trabajo.

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
- **interpretacion.txt**
  - Interpretacipon del resultado obtenido en Ex.py

## Ejercicio 3

- **Ex3.py**
  - Toma el archivo BLAST de salida y busca los primeros 10 hits. Realiza el alienamiento progresivo e iterativo con las 10 secuencias obtenidas del BLAST y la secuencia _query_.
  - input: archivo en BLAST
  - output: archivos de alineamiento progresivo con CLUSTAW y alineamiento iterativo con MUSCLE.

## Ejercicio 4

- **Ex4.py**
  - Toma el archivo `sequence.gb` y utiliza la función _getorf_ de EMBOSS para hallar los posibles ORF de la secuencia. También toma una archivo fasta y analiza los _motifs_ utilizando la base de datos de prosite.

  - input: archivo genebank y archivo fatsa
  - output: archvo de secuencias de aa para cada orf hallado y archivo de motifs.

## Ejercicio 5
- input: archivo Genbank con nucleótidos (`sequence.gb`) de la secuencia de interés
- output: archivo FASTA con _primers_ de la hebra directa y la hebra complementaria. 

- **utils.py**
  - Contiene las funciones correspondientes para lectura y escritura de archivos de tipo Genbank, Blast y Fasta. También incluye la importación de la librería _argparse_ que es utilizada a lo largo de todos los _scripts_.

# Diagrama de ejecución y comunicación de archivos

