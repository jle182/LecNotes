import requests
import os
import random
import time
# Define the API endpoint
endpoint = 'https://api.openai.com/v1/chat/completions'
# Define the API key
api_key = "INSERT KEY HERE"




# Define the directory path
with open("file_downloaded.txt", "r") as f:
    name = f.read()
with open("name_of_lecture.txt", "r") as file:
    question = file.read()
# Loop through all files in the directory
#for filename in sorted(os.listdir(directory)):
    # Read the transcript file
with open('Merged_Summaries.txt', 'r') as file:
    prompt = file.read()
    

prompt = "Create a detailed hierarchical outline of notes from an audio-to-text transcript of a "+question+" university lecture. Use a maximum of 800 words. Follow this consistent format: main topics with Roman numerals (I, II, III), subtopics with capital letters (A, B, C), key points with numbers (1, 2, 3), and nested bullet points with dashes (-). Here is the transcript merged together: " + "\"" + prompt + "\""
    # Define the headers

headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }

        # Define the payload
'''payload = {
            "message": prompt,
            "max_tokens": 8000,
            "temperature": .3,
            "model": "gpt-4"
        }
'''
payload = {
    "model": "gpt-4",
    "temperature": .3,
    "messages": [
        {"role": "system", "content": "You are a summarizer who takes an audio-to-text transcript and converts it into intelligentible, easy notes."},
        {"role": "user", "content": prompt},
    ]
}
        # Make the API request

response = requests.post(endpoint, headers=headers, json=payload)

        # Print the response
response_json = response.json()
#print(response_json)
#print(name)
answer = response_json['choices'][0]['message']['content']

output_filename = os.path.join('Final_Notes/', str(name[:-5])+ ".txt")

with open(output_filename, "w") as file:
    file.write(answer)     
print("#####################################################################################################")       
time.sleep(10)




