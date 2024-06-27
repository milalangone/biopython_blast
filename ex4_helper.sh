#!/bin/bash

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