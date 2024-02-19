import os

from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFDirectoryLoader, DirectoryLoader
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAI
from langchain import embeddings

from src.prompt import prompt_template_finance, prompt_template_technology, prompt_template_law
import warnings
warnings.filterwarnings("ignore")


load_dotenv()
client = OpenAI()
llm=OpenAI(max_tokens=1024)
embedding = embeddings.OpenAIEmbeddings()


def store_index(data_path,persist_directory):
    loader = PyPDFDirectoryLoader(data_path)
    data = loader.load()
    vectordb = Chroma.from_documents(documents=data,embedding=embedding,persist_directory=persist_directory)
    # persiste the database to disk
    vectordb.persist()
    vectordb = None


def select_database(input):
    if input == "finance":
        database = os.getenv("PERSIST_DIRECTORY_FINANCE")
    elif input == "technology":
        database = os.getenv("PERSIST_DIRECTORY_TECHNOLOGY")
    elif input == "law":
        database = os.getenv("PERSIST_DIRECTORY_LAW")
    else:
        pass
    return database


def get_retriever(database):
    vectordb = Chroma(persist_directory=database,embedding_function=embedding)
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

