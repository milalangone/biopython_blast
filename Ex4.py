import urllib.request
import os
import subprocess
import utils
import argparse

url_prosite = "https://ftp.expasy.org/databases/prosite/prosite.dat"
ruta_archivo = "prosite.dat"

if os.path.isfile(ruta_archivo):
    print(f"El archivo {ruta_archivo} ya está descargado")
else:
    try:
        urllib.request.urlretrieve(url_prosite,ruta_archivo)
        print("Archivo prosite.dat descargado exitosamente")
    except urllib.error.URLError as e:
        print(f"Error al descargar el archivo: {e}")
        exit()

ap = utils.argparse.ArgumentParser()
ap.add_argument('-i', '--input', help="Archivo de secuencia de nucleótidos para buscar los ORFs")
args = vars(ap.parse_args())
output_file = 'found_domains.patmatmotifs'

if os.path.isfile(ruta_archivo):
    if args['input']:
        orf_output_file = "orfs.fasta"
        getorf_cmd = ['getorf', '-sequence', args['input'], '-outseq', orf_output_file]
        result = subprocess.run(getorf_cmd, stderr=subprocess.PIPE)

        if result.returncode == 0:
            print(f"ORFs calculados y guardados en {orf_output_file}")
        else:
            print("Se produjo un error al calcular los ORFs. Detalle del error: ")
            print(result.stderr.decode())
            exit()

        patmotif = f"patmatmotifs -sequence {orf_output_file} -outfile {output_file}"
        with open(output_file, "w") as file:
            result = subprocess.run(patmotif, shell=True, stderr=subprocess.PIPE, stdout=file)
        if result.returncode == 0:
            print(f'Analisis de dominios completado. Se guardaron en el archivo {output_file}')
        else:
            print("Se produjo un error al analizar los dominios. Detalle del error: ")
            print(result.stderr.decode())
            
else:
    print(f"El archivo {ruta_archivo} no se descargò correctamente")

