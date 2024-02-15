import os
import traceback
from flask import Flask ,render_template, request, redirect, url_for
from langchain.chains.question_answering import load_qa_chain
from langchain_community.llms import OpenAI
from langchain import embeddings
from langchain.prompts import PromptTemplate
from langchain_community.vectorstores import Chroma
from dotenv import load_dotenv
import datetime
import warnings
warnings.filterwarnings("ignore")
from src.prompt import prompt_template

app = Flask(__name__)

load_dotenv()
client = OpenAI()
llm=OpenAI(max_tokens=1024)
embeddings = embeddings.OpenAIEmbeddings()
persist_directory=os.getenv("PERSIST_DIRECTORY")

vectordb = Chroma(persist_directory=persist_directory,embedding_function=embeddings)
print(vectordb)
retriever = vectordb.as_retriever(search_type="mmr", search_kwargs={"k":1})

@app.route("/")
def index():
    return render_template('chat.html')


@app.route("/get",methods=["GET","POST"])
def home():
    question = request.form['msg']
    docs = retriever.get_relevant_documents(question,max_tokens=1024)
    prompt = PromptTemplate(template = prompt_template, input_variables = ["context", "question"],max_tokens=1024)
    chain = load_qa_chain(llm, chain_type="stuff", prompt=prompt)
    response = chain(
        {"input_documents":docs, "question": question}
        , return_only_outputs=True)
    return str(response['output_text'])

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=10000) 