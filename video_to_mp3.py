import whisper

import os
import subprocess
files = os.listdir("Rest API tutorial")

for file in files:
    tutorial_number = file.split("#")[1].replace(".mp4", "").strip()
    file_name = os.path.splitext(file.split("#")[0].strip())[0]
    # print(f"Tutorial Number: {tutorial_number}, File Name: {file_name}")
    subprocess.run(["ffmpeg", "-i", f"Rest API tutorial/{file}", f"audios/{tutorial_number}_{file_name}.mp3"])