# 🤖 RAG Course Assistant

A Retrieval-Augmented Generation (RAG) based AI assistant that answers questions from programming course videos using semantic search, embeddings, and a locally running Large Language Model.

## 📌 Overview

This project builds a local RAG pipeline that converts programming course videos into searchable knowledge and uses the retrieved context to generate answers to user questions.

The workflow includes:

- Converting course videos into audio
- Transcribing audio into text using Whisper
- Processing and chunking transcripts
- Merging smaller chunks to improve context quality
- Creating text embeddings using `bge-m3`
- Finding relevant chunks using Cosine Similarity
- Retrieving the most relevant transcript chunks
- Building a context-aware prompt
- Generating answers using Llama 3.2 through Ollama

## 🛠️ Technologies Used

- Python
- NumPy
- Pandas
- Scikit-learn
- Joblib
- Whisper
- FFmpeg
- Ollama
- bge-m3
- Llama 3.2
- JSON

## 🧠 RAG Components

The project uses the following main components:

1. **Whisper** — Converts course audio into text transcripts.
2. **Chunk Processing** — Processes and merges transcript sections into useful context.
3. **bge-m3** — Generates vector embeddings for transcript chunks and user questions.
4. **Cosine Similarity** — Measures similarity between the question embedding and transcript embeddings.
5. **Llama 3.2** — Generates the final answer using the retrieved course context.
6. **Ollama** — Runs the embedding and language models locally.

## 🔄 Project Workflow

```text
Course Videos
      ↓
Audio Extraction
      ↓
Speech-to-Text
      ↓
Transcript JSON
      ↓
Chunk Processing
      ↓
Chunk Merging
      ↓
Text Embeddings
      ↓
Semantic Search
      ↓
Top Relevant Chunks
      ↓
Context + User Question
      ↓
Llama 3.2 via Ollama
      ↓
Final Answer
```

## 🔍 Semantic Retrieval

When a user asks a question, the question is converted into an embedding using `bge-m3`.

The system then calculates **Cosine Similarity** between the question embedding and the stored transcript embeddings.

The most similar chunks are selected and provided as context to the language model.

```text
User Question
      ↓
Question Embedding
      ↓
Cosine Similarity
      ↓
Top Relevant Chunks
      ↓
Context
      ↓
LLM
```

## 🧩 Chunk Processing

During development, I found that very small transcript chunks often provided incomplete context.

To improve retrieval quality, consecutive transcript chunks are merged before creating embeddings.

For example:

```text
Small Chunks
    ↓
Chunk 1
Chunk 2
Chunk 3
Chunk 4
Chunk 5
    ↓
Merged Chunk
```

This provides the language model with more coherent context when answering questions.

## 💬 Example

```text
Ask A Question: How does a REST API really work?

Top Relevant Chunks:
...

Final Answer:
[Answer generated using the retrieved course context]
```

The system uses the retrieved transcript context as the basis for generating the answer.

## 📁 Project Structure

```text
rag-course-assistant/
│
├── Merge_chunks.py
├── embed_chunks.py
├── mp3_to_jsons.py
├── process_incoming.py
├── video_to_mp3.py
├── README.md
└── .gitignore
```

> Course videos, extracted audio, transcript JSON files, generated embeddings, temporary outputs, and unused demonstration files are excluded from the repository.

## ⚙️ Requirements

- Python 3.11+
- FFmpeg
- Whisper
- Ollama
- `bge-m3`
- `llama3.2`

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/Manisha7530/rag-course-assistant.git
cd rag-course-assistant
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
pip install numpy pandas scikit-learn joblib
```

Install and configure Whisper and FFmpeg according to your system.

### 4. Set Up Ollama

Make sure Ollama is installed and running locally.

Pull the required models:

```bash
ollama pull bge-m3
ollama pull llama3.2
```

### 5. Run the RAG Pipeline

After preparing the transcript data and embeddings:

```bash
python process_incoming.py
```

Enter your question when prompted:

```text
Ask A Question: How does a REST API really work?
```

The system retrieves the most relevant transcript chunks and generates an answer using the local LLM.

## 💡 What I Learned

Building this project helped me understand:

- How Retrieval-Augmented Generation works
- How text embeddings represent semantic information
- How semantic search can retrieve relevant information
- How Cosine Similarity can be used for retrieval
- Why chunk size and context quality matter in RAG
- How retrieved context can be passed to an LLM
- How to run LLM inference locally using Ollama
- How preprocessing affects the quality of RAG responses

## 📈 Future Improvements

- Improve chunking strategies
- Add metadata filtering
- Implement reranking
- Add source and timestamp citations
- Improve retrieval evaluation
- Add conversation history
- Build a FastAPI backend
- Create a web interface
- Add RAG evaluation metrics

## 👩‍💻 Author

**Manisha Kumari**

GitHub: [Manisha7530](https://github.com/Manisha7530)

---

⭐ If you find this project interesting, feel free to explore the repository and give it a star.

