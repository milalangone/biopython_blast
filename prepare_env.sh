#!/bin/bash

# Check if python3 is installed
if command -v python3 -ne "" &>/dev/null; then
    echo "Python3 is already installed."
else
  echo "Python3 is not installed. Installing Python3..."
  sudo apt update
  sudo apt install python3 -y 
fi
if [ $? -ne 0 ]; then
  exit 1
fi

# Check if pip is installed
if command -v pip3 -ne "" &>/dev/null; then
  echo "pip is not installed. Installing pip..."
  sudo apt install python3-pip -y
else
  echo "pip is already installed."
fi
if [ $? -ne 0 ]; then
  exit 1
fi

# Install or upgrade Biopython
echo "Installing or upgrading Biopython..."
sudo -H pip3 install --upgrade biopython
echo "Biopython installation completed."
if [ $? -ne 0 ]; then
  exit 1
fi

echo "Environment is properly prepared."