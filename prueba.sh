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

# Check if pip is installed
pip3 --version 
if [ $? -ne 0 ]; then
  echo "pip3 is not installed. Installing pip..."
  sudo apt install python3-pip -y 
else
  echo "pip3 is already installed."
fi

### CHECK FOR NEEDED LIBRARIES ### 

python3 -c "import Bio" 
if [ $? -ne 0 ]; then
  echo "Biopython is not installed. Installing Biopython..."
  pip3 install biopython -y
else
  echo "Biopython is already installed."
fi

python3 -c "import pandas"
if [ $? -ne 0 ]; then
  echo "Pandas is not installed. Installing Pandas..."
  pip3 install pandas -y
else
  echo "Pandas is already installed."
fi
