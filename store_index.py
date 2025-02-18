from src.helper import load_pdf_file, text_split, download_hugging_face_embeddings
from pinecone.grpc import PineconeGRPC as Pinecone
from pinecone import ServerlessSpec
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone
from pinecone import Pinecone
from dotenv import load_dotenv
import os
import huggingface_hub
import sentence_transformers

load_dotenv()


PINECONE_API_KEY=os.environ.get('PINECONE_API_KEY')
#OPENAI_API_KEY=os.environ.get('OPENAI_API_KEY')


extracted_data=load_pdf_file(data='C:/Users/atq765/GenAI/End-to-end-Scholar-Chatbot-using-Llama2/data/')

text_chunks=text_split(extracted_data)

embeddings = download_hugging_face_embeddings()

#from pinecone.grpc import PineconeGRPC as Pinecone
#from pinecone import Pinecone
#from pinecone import ServerlessSpec


#pc = Pinecone(api_key=PINECONE_API_KEY)

pc = Pinecone(api_key=PINECONE_API_KEY)

              


index_name = "scholar-chatbot"



from langchain_pinecone import PineconeVectorStore

docsearch = PineconeVectorStore.from_documents(
    documents=text_chunks,
    index_name=index_name,
    embedding=embeddings, 
)

