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


echo "Running pipeline..."
echo "- EJ 1" 
echo "- EJ 1" >> $LOG_FILE
python3 Ex1.py -s sequence.gb >> $LOG_FILE
python3 best_rf.py -t "fasta_output.fasta" >> $LOG_FILE
echo "- EJ 2" 
echo "- EJ 2 local" >> $LOG_FILE
python3 Ex2_local.py -f "fasta_longest.fasta" >> $LOG_FILE
# # If server blast is wanted, uncomment next 2 lines:
# echo "- EJ 2 web server" >> $LOG_FILE
# python3 Ex2_server.py -f "fasta_longest.fasta" >> $LOG_FILE
echo "- EJ 3" 
echo "- EJ 3" >> $LOG_FILE
python3 Ex3.py -q "fasta_longest.fasta" >> $LOG_FILE
echo "- EJ 4" 
echo "- EJ 4" >> $LOG_FILE
python3 Ex4.py -i sequence.gb -s sequences_10.fasta >> $LOG_FILE
echo "- EJ 5" 
echo "- EJ 5" >> $LOG_FILE
python3 Ex5.py -s sequence.gb -j parameters.json >> $LOG_FILE
