from flask import Flask, render_template, request
from src.helper import download_hugging_face_embeddings
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain_pinecone import Pinecone  # Updated import for Pinecone integration
from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers
from langchain.chains import RetrievalQA
from dotenv import load_dotenv
import os

app = Flask(__name__)

# Load environment variables from .env file
load_dotenv()

# Fetch API keys and settings from environment variables
PINECONE_API_KEY = os.getenv('PINECONE_API_KEY')
index_name = "scholar-chatbot"  # Replace with your Pinecone index name

# Define your prompt template
prompt_template = (
    "Context:\n{context}\n\n"
    "Question:\n{question}\n\n"
    "Answer:"
)

# Download Hugging Face embeddings (ensure your helper returns a valid embeddings object)
embeddings = download_hugging_face_embeddings()

# Load the Pinecone index using the updated Pinecone class (the API key and environment are read from env variables)
docsearch = Pinecone.from_existing_index(index_name, embeddings)

# Define your PromptTemplate for QA
PROMPT = PromptTemplate(template=prompt_template, input_variables=["context", "question"])

# Define the chain type kwargs
chain_type_kwargs = {"prompt": PROMPT}

# Initialize the language model (CTransformers with Llama2)
llm = CTransformers(
    model='model/llama-2-7b-chat.ggmlv3.q8_0.bin',  # Ensure path to model is correct
    model_type='llama',
    config={'max_new_tokens': 256, 'temperature': 0.01}
)

# Set up the RetrievalQA chain
qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=docsearch.as_retriever(search_kwargs={'k': 2}),
    return_source_documents=True,
    chain_type_kwargs=chain_type_kwargs
)

# Define routes for Flask app
@app.route("/")
def index():
    return render_template('chat.html')  # Ensure this file exists in your templates folder

@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]  # Get the message from the form
    input_query = msg  # Renamed from 'input' to avoid conflicts with the built-in function
    print(f"Input query: {input_query}")
    
    # Get the result from the QA chain
    result = qa({"query": input_query})
    print(f"Response: {result['result']}")
    return str(result["result"])

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
