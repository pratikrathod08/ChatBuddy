from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFDirectoryLoader , DirectoryLoader
# from langchain_openai import OpenAIEmbeddings
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAI
from langchain import embeddings
from src.prompt import prompt_template_finance , prompt_template_technology , prompt_template_law

import os
import warnings
warnings.filterwarnings("ignore")

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

def select_db(input):
    if input == "finance":
        db = os.getenv("PERSIST_DIRECTORY_FINANCE")
    elif input == "technology":
        db = os.getenv("PERSIST_DIRECTORY_TECHNOLOGY")
    elif input == "law":
        db = os.getenv("PERSIST_DIRECTORY_LAW")
    else:
        pass
    
    return db

# db = select_db("finance")
# print(db)

def get_retriever(db):
    vectordb = Chroma(persist_directory=db,embedding_function=embedding)
    retriever = vectordb.as_retriever(search_type="mmr", search_kwargs={"k":1})
    return retriever

def select_prompt_template(persist_directory):
    if persist_directory == os.getenv("PERSIST_DIRECTORY_FINANCE"):
        prompt_template = prompt_template_finance
    elif persist_directory == os.getenv("PERSIST_DIRECTORY_TECHNOLOGY"):
        prompt_template = prompt_template_technology
    elif persist_directory == os.getenv("PERSIST_DIRECTORY_LAW"):
        prompt_template = prompt_template_law

    else:
        pass

    return prompt_template

