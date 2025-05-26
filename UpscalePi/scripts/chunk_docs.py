import os
import tiktoken
import pickle

def load_all_docs(folder=None):
    if folder is None:
        # Go up two dirs from this script, then into docs
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        folder = os.path.join(base_dir, "docs")

    texts = []
    for filename in os.listdir(folder):
        if filename.endswith(".json"):
            path = os.path.join(folder, filename)
            with open(path, "r", encoding="utf-8") as f:
                texts.append(f.read())
    return "\n\n".join(texts)

def chunk_text(text, max_tokens=500):
    tokenizer = tiktoken.get_encoding("cl100k_base")
    tokens = tokenizer.encode(text)
    chunks = []
    start = 0
    while start < len(tokens):
        end = min(start + max_tokens, len(tokens))
        chunk_tokens = tokens[start:end]
        chunk_text = tokenizer.decode(chunk_tokens)
        chunks.append(chunk_text)
        start = end
    return chunks

if __name__ == "__main__":
    print("Loading all JSON docs from the correct docs folder...")
    full_text = load_all_docs()

    print(f"Loaded full text length: {len(full_text)} characters")
    print("Chunking text into pieces of max 500 tokens each...")
    chunks = chunk_text(full_text, max_tokens=500)

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    output_path = os.path.join(base_dir, "chunks.pkl")
    with open(output_path, "wb") as f:
        pickle.dump(chunks, f)

    print(f"Saved {len(chunks)} chunks to {output_path}")
