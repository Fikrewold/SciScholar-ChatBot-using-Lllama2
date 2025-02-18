from pinecone.grpc import PineconeGRPC as Pinecone
from src.helper import load_pdf_file, text_split, download_hugging_face_embeddings
#from pinecone import Pinecone
from pinecone import ServerlessSpec
import os


extracted_data=load_pdf_file(data='C:/Users/atq765/GenAI/End-to-end-Scholar-Chatbot-using-Llama2/data/')

text_chunks = text_split(extracted_data)

PINECONE_API_KEY=os.environ.get('PINECONE_API_KEY')


pc = Pinecone(api_key=PINECONE_API_KEY)



index_name = "scholar-chatbot5"

pc.create_index(
    name=index_name,
    dimension=384, # Replace with your model dimensions
    metric="cosine", # Replace with your model metric
    spec=ServerlessSpec(
        cloud="aws",
        region="us-east-1"
    ) 
)



os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
#os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

from langchain_pinecone import PineconeVectorStore

docsearch = PineconeVectorStore.from_documents(
    documents=text_chunks,
    index_name=index_name,
    embedding=embeddings, 
)