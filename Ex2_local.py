import subprocess
import utils


def run_blast(sequence, output):
    blast_command = [
        "blastp",
        "-query", sequence,
        "-db", "swissprot",
        "-out", output,
        "-outfmt", "5" #XML output
    ]
    subprocess.run(blast_command)

ap = utils.argparse.ArgumentParser()
ap.add_argument('-f', help='Para ingresar la o las secuencias con mejor Reading Frame en formato Fasta')
args = vars(ap.parse_args())

# Verificar si se proporcionó el argumento '-f'
if args['f']:
    run_blast(args['f'], "local_blast_result.out")

    print("BLAST completado y resultados guardados.")
    
else:
    print("Error: Debes proporcionar al menos un archivo de secuencia con el argumento '-f'.")
