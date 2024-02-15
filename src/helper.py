from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFDirectoryLoader , DirectoryLoader
# from langchain_openai import OpenAIEmbeddings
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAI
from langchain import embeddings
import os

load_dotenv()
client = OpenAI()

llm=OpenAI(max_tokens=1024)
embedding = embeddings.OpenAIEmbeddings()

# persist_directory=os.getenv("PERSIST_DIRECTORY")




def store_index(data_path,persist_directory):
    loader = PyPDFDirectoryLoader(data_path)
    data = loader.load()
    vectordb = Chroma.from_documents(documents=data,embedding=embedding,persist_directory=persist_directory)
    # persiste the db to disk
    vectordb.persist()
    vectordb = None

