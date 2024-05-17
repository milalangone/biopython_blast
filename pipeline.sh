# If environment is not prepared, prepare it or stop execution if needed
sh prepare_env.sh
if [ $? -ne 0 ]; then
  echo "Error in prepare_env.sh - Something could not be installed/upgraded - Check before running this script again."
  exit 1
else
  echo "Environment is ready."
fi


# Create log file and give permissions
LOG_FILE="log.log"
touch $LOG_FILE
chmod 777 $LOG_FILE

# Run the pipeline with unique timestamp for each execution
fecha_actual=$(date)
echo ">>$fecha_actual" >> $LOG_FILE

python3 Ex1.py -s sequence.gb >> $LOG_FILE
python3 best_rf.py -t "fasta_output.fasta" >> $LOG_FILE
#python3 Ex2.py -f "fasta_longest.fasta" >> $LOG_FILE
#python3 Ex3.py -q "fasta_longest.fasta" >> $LOG_FILE
python3 Ex4.py -i sequence.fasta >> $LOG_FILE

python3 Ex5.py -s sequence.gb -j 'parameters.json' >> $LOG_FILE