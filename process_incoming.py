import requests
import joblib
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def create_embedding(text_list):
    r = requests.post("http://localhost:11434/api/embed", json={
        "model": "bge-m3", 
        "input": text_list})

    embedding = r.json()["embeddings"]
    return embedding

def inference(prompt):
    r = requests.post("http://localhost:11434/api/generate", json={
        "model": "llama3.2", 
        "prompt": prompt,
        # "suffix": "return response",
        "stream": False,})
        # "max_new_tokens": 512})
    response = r.json()
    print(response)
    return response


df = joblib.load("embeddings.joblib")

incoming_query = input("Ask A Question: ")
question_embedding = create_embedding([incoming_query])[0]


# Find similarities of question_embedding with other embweddings
# print(np.vstack(df["embedding"].values))
# print(np.vstack(df["embedding"].shape))

similarities = cosine_similarity(np.vstack(df["embedding"]), [question_embedding]).flatten()
top_results = 3
max_indx = similarities.argsort()[::-1][:top_results]  # Get top 5 most similar chunks
print(f"Top {top_results} most similar chunks:")

new_df = df.loc[max_indx]

context = "\n\n".join(
    f"""
Lesson: {row['title']}
Timestamp: {row['start']} - {row['end']}
Transcript:
{row['text']}
"""
    for _, row in new_df.iterrows()
)
# print(context)

prompt = f'''
You are an AI teaching assistant for a programming course.

Your task is to answer the user's question using ONLY the information contained
in the provided video transcript.

IMPORTANT:
- Understand the transcript before answering.
- Do NOT copy sentences directly from the transcript.
- Do NOT simply repeat or quote the transcript.
- Synthesize information from multiple relevant chunks when necessary.
- Explain the concept in your own words.
- Give a clear, educational answer suitable for a beginner.
- If the context contains multiple relevant points, combine them into one coherent explanation.
- Use bullet points or numbered points when they improve clarity.
- You may give a small example ONLY if that example is directly supported by the context.
- Do NOT use outside/general knowledge.
- If the provided context does not contain enough information to answer the question, say:
  "I don't know based on the provided course material."

COURSE CONTEXT:
{context}
--------------------------------------------------------
USER QUESTION:
{incoming_query}

Now answer the question clearly and naturally.
'''
with open("prompt.txt", "w") as f:
    f.write(prompt)

response = inference(prompt)["response"]
print(response)

with open("response.txt", "w") as f:
    f.write(response)