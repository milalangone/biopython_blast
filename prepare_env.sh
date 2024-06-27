#!/bin/bash

### CHECK FOR PROGRAMMING LANGUAGES AND PKG MANAGERS ###

# Check if python3 version
python3 --version 
if [ $? -ne 0 ]; then
  echo "Python3 is not installed. Installing Python3..."
  sudo apt update
  sudo apt install python3 -y
else
  echo "Python3 is already installed."
fi

sudo apt install python3-pip
# TO GENERATE THE FILE: Install locally all reqs and then run `pip freeze > requirements.txt`
pip install -r requirements.txt

### CHECK FOR NEEDED TOOLS ### 

blastp --version 
if [ $? -ne 0 ]; then
  echo "Blastp is not installed. Installing Blastp..."
  sudo apt update
  sudo apt-get install ncbi-blast+
else
  echo "Blastp is already installed."
fi

perl -v
if [ $? -ne 0 ]; then
  echo "Perl is not installed. Installing Perl..."
  sudo apt update
  sudo apt-get install perl
else
  echo "Perl is already installed."
fi

if [ ! -f "swissprot"]; then
  echo "Installing SwissProt..."
  update_blastdb --decompress swissprot
else
  echo "SwissProt is already installed."
fi

clustalo --version 
if [ $? -ne 0 ]; then
  echo "Clustalo is not installed. Installing Clustalo..."
  sudo apt update
  sudo apt-get install clustalo
else
  echo "Clustalo is already installed."
fi

muscle -version 
if [ $? -ne 0 ]; then
  echo "Muscle is not installed. Installing Muscle..."
  sudo apt update
  sudo apt-get install muscle
else
  echo "Muscle is already installed."
fi

embossdata --version
if [ $? -ne 0 ]; then
  echo "EMBOSS is not installed. Installing EMBOSS..."
  sudo apt update
  sudo apt-get install emboss
else
  echo "EMBOSS is already installed."
fi

export EMBOSS_DATA=$HOME/emboss_data
mkdir -p $HOME/emboss_data/PROSITE

# Define the URLs and the local file names
PROSITE_DAT_URL="https://ftp.expasy.org/databases/prosite/prosite.dat"
PROSITE_DOC_URL="https://ftp.expasy.org/databases/prosite/prosite.doc"
PROSITE_DIR="$HOME/emboss_data/PROSITE"  # Directory to store EMBOSS PROSITE data

# Download the PROSITE database files if they don't exist
if [ ! -f "$PROSITE_DIR/prosite.dat" ]; then
    wget $PROSITE_DAT_URL -O $PROSITE_DIR/prosite.dat
fi
if [ ! -f "$PROSITE_DIR/prosite.doc" ]; then
    wget $PROSITE_DOC_URL -O $PROSITE_DIR/prosite.doc
fi

# Move to the PROSITE directory
cd $PROSITE_DIR

# Run prosextract to process the PROSITE database
prosextract .
if [ $? -ne 0 ]; then
    echo "Error processing PROSITE database with prosextract"
    exit 1
fi