import os
import requests
from pinecone import Pinecone
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer

load_dotenv(dotenv_path=os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env'))

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_ENV = os.getenv("PINECONE_ENV")
INDEX_NAME = os.getenv("PINECONE_INDEX_NAME")

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

pc = Pinecone(api_key=PINECONE_API_KEY)
index = pc.Index(INDEX_NAME)

def get_relevant_chunks(query, top_k=5):
    embedding = model.encode([query]).tolist()
    results = index.query(vector=embedding[0], top_k=top_k, include_metadata=True)
    chunks = [match["metadata"]["text"] for match in results["matches"]]
    return "\n".join(chunks)

def ask_llama2(prompt):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama2",
            "prompt": prompt,
            "stream": False
        }
    )
    return response.json()["response"]

def main():
    print("📘 Ask a question (or type 'exit'):")
    while True:
        query = input("\n🧠 You: ")
        if query.lower() in ['exit', 'quit']:
            break

        context = get_relevant_chunks(query)
        full_prompt = f"""Answer the question using the following context:\n\nContext:\n{context}\n\nQuestion: {query}\nAnswer:"""
        answer = ask_llama2(full_prompt)

        print(f"\n🤖 LLaMA 2: {answer.strip()}")

if __name__ == "__main__":
    main()
