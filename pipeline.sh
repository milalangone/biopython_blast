touch Log.log
chmod 777 Log.log

fecha_actual=$(date +'%d/%m/%y %H:%M')

echo ">>$fecha_actual" >> Log.log

python3 Ex1.py -s transcript_3.gb >> "Log.log"
python3 best_rf.py -t "fasta_output.fasta" >> "Log.log"
python3 Ex2.py -f "fasta_longest.fasta"
python3 Ex3.py
