# Scholar-Chatbot-using-Llama2

Scholar Chatbot is an AI-powered assistant designed to help researchers, students, and academics interact with scholarly documents. Built using Llama 2 and CTransformers, this chatbot can extract relevant content from PDFs and provide contextually accurate answers to research-related queries. It supports natural language processing for intelligent search and conversation, making it a valuable tool for navigating academic publications.

https://private-user-images.githubusercontent.com/40051036/415466563-bfa7a5e2-d156-48e5-92f8-4c6b698cba44.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDEyMDQ1ODUsIm5iZiI6MTc0MTIwNDI4NSwicGF0aCI6Ii80MDA1MTAzNi80MTU0NjY1NjMtYmZhN2E1ZTItZDE1Ni00OGU1LTkyZjgtNGM2YjY5OGNiYTQ0LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTAzMDUlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwMzA1VDE5NTEyNVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTMwOWJiMDg2MWNlYzU3ZTNlYTg2YzkwM2IxMGNiMWM5Njc4Zjc5OTliZmI3Y2ZiMDE4ZWUzNTA3NzA4NTM5MzQmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.mcGI7bntM5KXXoG0crhcF1fnLCDV0E4R_Y6vXf9xWQk

Features:\
✅ AI-driven question answering based on research papers\
✅ PDF content extraction for scholarly insights\
✅ Customizable prompt engineering for better responses\
✅ Local and cloud deployment options\
✅ Optimized for efficiency and accuracy

# How to run?
### STEPS:

Clone the repository

```bash
Project repo: https://github.com/Fikrewold/SciScholar-ChatBot-using-Lllama2.git
```

### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n ScholarBot python=3.9 -y
```

```bash
conda activate mchatbot
```

### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


### Create a `.env` file in the root directory and add your Pinecone credentials as follows:

```ini
PINECONE_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
PINECONE_API_ENV = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```


### Download the quantize model from the link provided in model folder & keep the model in the model directory:

```ini
## Download the Llama 2 Model:

llama-2-7b-chat.ggmlv3.q4_0.bin


## From the following link:
https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main

```

```bash
# run the following command
python store_index.py
```

```bash
# Finally run the following command
python app2.py
```

Now,
```bash
open up localhost:
```


### Techstack Used:

- Python
- LangChain
- Flask
- Meta Llama2
- Pinecone


