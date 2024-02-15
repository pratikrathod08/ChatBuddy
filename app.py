import os
import traceback
from flask import Flask ,render_template, request, redirect, url_for , jsonify
from langchain.chains.question_answering import load_qa_chain
from langchain_community.llms import OpenAI
from langchain_community.embeddings import OpenAIEmbeddings
# from langchain import embeddings
from langchain.prompts import PromptTemplate
from langchain_community.vectorstores import Chroma
from dotenv import load_dotenv
import datetime
import warnings
warnings.filterwarnings("ignore")
# from src.prompt import prompt_template
from src.helper import select_db
from src.helper import get_retriever
from src.helper import select_prompt_template
import time

app = Flask(__name__)

load_dotenv()
client = OpenAI()
llm=OpenAI(max_tokens=1024)
embedding = OpenAIEmbeddings()
# persist_directory=os.getenv("PERSIST_DIRECTORY_FINANCE")
persist_directory = None

# vectordb = Chroma(persist_directory=persist_directory,embedding_function=embeddings)
# print(vectordb)
# retriever = vectordb.as_retriever(search_type="mmr", search_kwargs={"k":1})

@app.route("/")
def index():
    return render_template('chat.html')


@app.route("/get",methods=["GET","POST"])
def home():

    if request.is_json:
        data = request.get_json()
        button_value = data.get('button_value','')
        global persist_directory
        persist_directory = select_db(button_value)
        # print(persist_directory)

        return "hello"
    # if type(request.form['question']) == "str":
    #     global category
    #     category = request.form['category']
    # global persist_directory
    # persist_directory = select_db(category)

    # category = request.form['category']
    # global persist_directory
    # persist_directory = select_db(category)


    # retriever = get_retriever(persist_directory)

    # docs = retriever.get_relevant_documents(question,max_tokens=1024)
    # prompt = PromptTemplate(template = prompt_template, input_variables = ["context", "question"],max_tokens=1024)
    # chain = load_qa_chain(llm, chain_type="stuff", prompt=prompt)
    # response = chain(
    #     {"input_documents":docs, "question": question}
    #     , return_only_outputs=True)
    # return str(response['output_text'])

    if not request.is_json:
        question = request.form['msg']

        if persist_directory != None:
            retriever = get_retriever(persist_directory)
            docs = retriever.get_relevant_documents(question,max_tokens=1024)
            prompt_template = select_prompt_template(persist_directory)
            prompt = PromptTemplate(template = prompt_template, input_variables = ["context", "question"],max_tokens=1024)
            chain = load_qa_chain(llm, chain_type="stuff", prompt=prompt)
            response = chain(
                {"input_documents":docs, "question": question}
                , return_only_outputs=True)
            return str(response['output_text'])
        else:
            time.sleep(2)
            return "Hello please select category for help us to understand your statement and provide proper response"

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=10000) 