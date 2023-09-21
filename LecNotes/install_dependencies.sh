#!/bin/bash

# Install system dependencies
sudo apt update
sudo apt install -y ffmpeg

# Install Python libraries
pip install moviepy requests pydub SpeechRecognition

python3 create_folders.py

echo "All dependencies have been installed!"

