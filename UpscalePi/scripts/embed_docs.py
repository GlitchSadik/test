import os
import pickle
import pinecone
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env'))

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_ENV = os.getenv("PINECONE_ENV")
INDEX_NAME = os.getenv("PINECONE_INDEX_NAME")

pc = pinecone.Pinecone(api_key=PINECONE_API_KEY)

if INDEX_NAME not in pc.list_indexes(): #caution:""if INDEX_NAME not in pc.list_indexes().names():""changed here,can be problematic later
    from pinecone import ServerlessSpec
    pc.create_index(
        name=INDEX_NAME,
        dimension=384,
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region=PINECONE_ENV),
    )

index = pc.Index(INDEX_NAME)

with open("/Users/invictus/Desktop/Upscale/UpscalePi/chunks.pkl", "rb") as f:
    chunks = pickle.load(f)

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

batch_size = 100
for i in range(0, len(chunks), batch_size):
    batch_chunks = chunks[i : i + batch_size]
    embeddings = model.encode(batch_chunks).tolist()
    vectors = [
        (f"chunk-{i+j}", embeddings[j], {"text": batch_chunks[j]})
        for j in range(len(batch_chunks))
    ]
    index.upsert(vectors)
    print(f"Uploaded batch {i//batch_size + 1} / {len(chunks)//batch_size + 1}")

print("All chunks embedded and uploaded to Pinecone!")
