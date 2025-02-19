# Scholar-Chatbot-using-Llama2

Scholar Chatbot is an AI-powered assistant designed to help researchers, students, and academics interact with scholarly documents. Built using Llama 2 and CTransformers, this chatbot can extract relevant content from PDFs and provide contextually accurate answers to research-related queries. It supports natural language processing for intelligent search and conversation, making it a valuable tool for navigating academic publications.

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
Project repo: https://github.com/
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


