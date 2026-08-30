import json
import whisper
import os

audios = os.listdir("audios")

model = whisper.load_model("turbo")

for audio in audios:
    number = audio.split("_")[0]
    title = audio.split("_")[1].split(".")[0]
    # print(f"Transcribing audio {number}-{title}...")
    result = model.transcribe(audio= f"audios/{audio}",
                              language="en",
                              task="transcribe",
                               word_timestamps=False )

    # print(result["segments"])
    chunks = []
    for segment in result["segments"]:  
        chunks.append({
            "number": number,
            "title": title,
            "id": segment["id"],
            "start": segment["start"],
            "end": segment["end"],
            "text": segment["text"]
        })

    # print(chunks)

    chunks_with_metadata = {"chunks": chunks, "text": result["text"]}

    with open(f"jsons/{audio}.json", "w") as f:
        json.dump(chunks_with_metadata, f)
    