import os

PROJECT_NAME = "UpscalePi"
structure = {
    "docs": [],
    "scripts": ["load_docs.py", "chunk_docs.py", "embed_docs.py", "query_agent.py"],
    "": ["main.py", "requirements.txt", "README.md"]
}

def create_structure():
    os.makedirs(PROJECT_NAME, exist_ok=True)
    
    for folder, files in structure.items():
        full_path = os.path.join(PROJECT_NAME, folder)
        os.makedirs(full_path, exist_ok=True)
        for file in files:
            with open(os.path.join(full_path, file), 'w') as f:
                f.write(f"# {file}\n")

    print(f"✅ Project structure for '{PROJECT_NAME}' created successfully!")

if __name__ == "__main__":
    create_structure()
