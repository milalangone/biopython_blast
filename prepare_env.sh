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

# TO GENERATE THE FILE: Install locally all reqs and then run `pip freeze > requirements.txt`
pip install -r requirements.txt

### CHECK FOR NEEDED TOOLS ### 

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
  sudo apt-get install myscle 
else
  echo "Muscle is already installed."
fi