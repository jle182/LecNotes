#!/bin/bash
rm ./split_files/*
rm ./text_files/trans*


#rm ./Final_Notes/*
rm Merged_Summaries.txt
echo "What is the Filename of your Lecture called?"
read user_input
echo "And what is the name of the Lecture?"
read user_input2
# Use the user input as the file path
file_path="../Downloads/$user_input"
echo "$user_input" > "file_downloaded.txt"

# Get the file name without extension
filename_without_ext="${user_input%.*}"

# Create the .wav and .mp3 file paths
wav_file_path="../Downloads/${filename_without_ext}.wav"
mp3_file_path="../Downloads/${filename_without_ext}.mp3"

while [ ! -f "$wav_file_path" ]; do
    if file "$file_path" | grep -q "ISO Media, MP4"; then
        echo "The file is a .mp4"
        python3 mp4_to_mp3.py
        user_input="${filename_without_ext}.mp3"
        file_path="$mp3_file_path"  # Update file_path to .mp3
    elif file "$file_path" | grep -q "Audio file"; then
        echo "The file is a .mp3"
        python3 mp3_to_wav.py
        user_input="${filename_without_ext}.wav"
        file_path="$wav_file_path"  # Update file_path to .wav
    else
        # File format isn't MP4 or MP3, check if it's WAV
        if file "$file_path" | grep -q "WAVE audio"; then
            echo "The file is a .wav"
            break  # Exit the loop since it's already a WAV
        else
            echo "File format not supported."
            break # Exit the script if the format isn't supported
        fi
    fi

    # Wait for a few seconds before checking again
    sleep 5
done



echo "The file has been converted to a .wav file."



# Specify the output file
output_file="name_of_lecture.txt"

# Save the user input to the output file
echo "$user_input2" > "$output_file"

# Print a confirmation message


echo "Starting Program.."
##clips lecture into increments of (whatever in brackets)
for i in {0..55}
do

x=$i; y=$((x * 60)); echo $y
x=$i; z=$((x * 60 + 60)); echo $z

hh=$z
RESULT=$(echo 00000$hh | tail -c 6)
k="./split_files/xoxox$RESULT.wav"
#echo $k
ffmpeg -i $wav_file_path -ss $y -to $z -c copy $k
done
#main.py changes the each of the clips into transcripts
python3 main.py

h="$wav_file_path.txt"
#NEED THISSSSSSSSSSS
cat ./text_files/*.txt >> Merged_Summaries.txt

python3 chatGPT.py

