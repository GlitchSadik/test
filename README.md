# UpscalePi

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/GlitchSadik/UpscalePi.git
cd UpscalePi
```
### 2. Create a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
```
### 3. Install Requirements
```bash
pip install -r UpscalePi/requirements.txt
```
### 4. Prepare Your .env File
#Create a .env file in the root folder with the following content and replace with your own credentials:
```bash
PINECONE_API_KEY=your_pinecone_api_key
PINECONE_ENV=your_pinecone_env
PINECONE_INDEX_NAME=your_pinecone_index
```
### 5. Run All Scripts Automatically
#Run the main script that will execute all required scripts in order:
```bash
python UpscalePi/main.py
```