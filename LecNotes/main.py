#DO NOT TOUCH
import logging
import time
import os
import speech_recognition as sr
from multiprocessing import Process, Queue

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


def transcribe_audio(audio_file, counter):
    r = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = r.record(source)
    try:
        transcript = r.recognize_google(audio)
    except sr.UnknownValueError:
        logging.warning(f"No audio detected in {audio_file}, OR UnknownValueError Skipping......")
        return
    filecounter=str(counter)
    filecounter=filecounter.zfill(5)
    with open('text_files/transcript'+filecounter+'.txt', 'w') as f:
        f.write(transcript + ' ')


def worker(queue):
    while True:
        task = queue.get()
        if task is None:  # if the sentinel value is received, stop the loop
            break
        audio_file, counter = task
        logging.info(f"Processing file {audio_file}")
        try:
            transcribe_audio(audio_file, counter)
        except (sr.UnknownValueError, sr.RequestError) as e:
            error_type = type(e).__name__
            logging.error(f"{error_type} {audio_file}: {e}")
            for j in range(3):
                logging.info(f"Retrying in 20 seconds... (retry {j + 1}/3)")
                time.sleep(20)
                try:
                    transcribe_audio(audio_file, counter)
                except (sr.UnknownValueError, sr.RequestError) as e:
                    logging.error(f"Error retrying: {e}")
                else:
                    break


# assign directory
directory = 'split_files'

# create a queue and add tasks to it
queue = Queue()
counter = 1
for i in sorted(os.listdir(directory)):
    audio_file = os.path.join(directory, i)
    if os.path.isfile(audio_file):
        queue.put((audio_file, counter))
        counter += 1


#worker multiplier
num_processes = 30
for i in range(num_processes):
    queue.put(None)

# start the worker processes
processes = []
for i in range(num_processes):
    p = Process(target=worker, args=(queue,))
    processes.append(p)
    p.start()

# wait for the worker processes to finish
for p in processes:
    p.join()
