import os

from dotenv import load_dotenv
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFDirectoryLoader , DirectoryLoader
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_openai import OpenAI
from langchain import embeddings
import warnings
warnings.filterwarnings("ignore")

from src.helper import store_index


list_of_Paths=["data/finance_and_banking",'data/computer_science_and_Technology',"data/Law"]
list_of_Persist_Dir = ["PERSIST_DIRECTORY_FINANCE","PERSIST_DIRECTORY_TECHNOLOGY","PERSIST_DIRECTORY_LAW"]


for i in range(len(list_of_Paths)):
    store_index(list_of_Paths[i],os.getenv(list_of_Persist_Dir[i]))