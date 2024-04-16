touch Log.log
chmod 777 Log.log

fecha_actual=$(date +'%d/%m/%y %H:%M')

echo ">>$fecha_actual" >> Log.log

echo "Previo al Ex1"
python3 Ex1.py -s sequence.gb >> "Log.log"
echo "Ex1.py ejecutado correctamente"
python3 best_rf.py -t "fasta_output.fasta" >> "Log.log"
echo "best_rf.py ejecutado correctamente"
python3 Ex2.py -f "fasta_longest.fasta"
echo "Ex2.py ejecutado correctamente"
python3 Ex3.py >> "Log.log"
echo "Ex3.py ejecutado correctamente"

