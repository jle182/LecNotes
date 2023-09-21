from moviepy.editor import *

with open("file_downloaded.txt", "r") as file:
    mp4 = file.read().strip()

# Replace the file extension with '.mp3'
last_period_index = mp4.rfind(".")
output_string = mp4[:last_period_index] + ".mp3"


# Write the new filename to the "file_downloaded.txt" file
with open("file_downloaded.txt", "w") as file:
    file.write(output_string)
# Load the video file
video = VideoFileClip('../Downloads/' + mp4)

# Extract the audio from the video and save it as an MP3 file
audio = video.audio

audio.write_audiofile('../Downloads/' + output_string)

# Close the video and audio files
video.close()
audio.close()
