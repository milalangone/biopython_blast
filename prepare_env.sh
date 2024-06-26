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
