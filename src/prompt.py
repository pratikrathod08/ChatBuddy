from langchain.prompts import PromptTemplate


prompt_template_finance = """
Answer question as detailed as possible from the provided context,don't make answer yourself and answer only from given context if the answer is not in
provided context, just say, "Answer is not available in the context kindly ask questions related to finance and banking", don't provide the wrong answer or not to try answer from yourself.\n\n

if somebody greetings then say "Hello! Thank you for greeting me. How can i assist you?".
Context:\n {context}?\n
Question: \n{question}\n

Answer:
"""

prompt_template_technology = """
Answer the question as detailed as possible from the provided context, don't make answer from youself and answer only from given context if the answer is not in
provided context, just say "Answer is not available in the context kindly ask questions related to computer science and technology", don't provide the wrong answer or not to try answer from yourself.\n\n

if somebody greetings then say "Hello! Thank you for greeting me. How can i assist you?".
Context:\n {context}?\n
Question: \n{question}\n

Answer:
"""

prompt_template_law = """
Answer the question as detailed as possible from the provided context, don't make answer from youself and answer only from given context if the answer is not in
provided context just say, "Answer is not available in the context kindly ask questions related to law and legal", don't provide the wrong answer or not to try answer from yourself.\n\n

if somebody greetings then say "Hello! Thank you for greeting me. How can i assist you?".
Context:\n {context}?\n
Question: \n{question}\n

Answer:
"""