from pydub import AudioSegment

def convert_mp3_to_wav(input_path):
    """Converts an MP3 file to WAV format and returns the path to the WAV file."""
    
    # Ensure the input file has the correct extension
    if not input_path.endswith(".mp3"):
        raise ValueError("Input file is not an MP3 file.")
    
    # Construct the output file path
    output_path = input_path.rsplit(".", 1)[0] + ".wav"
    
    # Load and convert the audio
    audio = AudioSegment.from_file(input_path, format="mp3")
    audio.export(output_path, format="wav")
    
    return output_path

# Read the input file path from 'file_downloaded.txt'
with open("file_downloaded.txt", "r") as file:
    input_file = file.read().strip()

# Prepend the directory path
input_path = "../Downloads/" + input_file

try:
    output_path = convert_mp3_to_wav(input_path)
    print(f"Converted {input_file} to {output_path}.")
except Exception as e:
    print(f"Error: {e}")

# Optionally, write the WAV file path to 'file_downloaded.txt'
# with open("file_downloaded.txt", "w") as file:
#     file.write(output_path)
