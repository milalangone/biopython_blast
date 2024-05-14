import urllib.request
import os

'''
Parte 1 del ej 4:
    Escribir un script que llame a algún programa EMBOSS para que realice algún 
    análisis sobre la una secuencia de nucleótidos fasta (del Ej. 1). Por ejemplo 
    que calcule los ORF y obtenga las secuencias de proteínas posibles.
'''
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

if os.path.isfile(ruta_archivo):
    '''
    Parte 2 ej 4:
        Llamado a otro programa EMBOSS realizar el análisis de dominios de 
        las secuencias de aminoácidos obtenidas y escribir los resultados 
        en un archivo de salida.
    '''
    print("jaja")
else:
    print(f"El archivo {ruta_archivo} no se descargò correctamente")

    