from langchain.prompts import PromptTemplate


prompt_template_finance = """
Answer the finance and banking related question as detailed as possible from the provided context, and answer only from given context if the answer is not in
provided context just say, "Answer is not available in the context kindly ask questions related to finance and banking", don't provide the wrong answer or not to try answer from yourself.\n\n

if somebody greetings then appriciate them and ask them how to help them regarding finance and banking.
Context:\n {context}?\n
Question: \n{question}\n

Answer:
"""

prompt_template_technology = """
Answer the computer science and information technology related question as detailed as possible from the provided context, and answer only from given context if the answer is not in
provided context just say, "Answer is not available in the context kindly ask questions related to technology", don't provide the wrong answer or not to try answer from yourself.\n\n

if somebody greetings then appriciate them and ask them how to help them regarding finance and banking.
Context:\n {context}?\n
Question: \n{question}\n

Answer:
"""

prompt_template_law = """
Answer the law related question as detailed as possible from the provided context, and answer only from given context if the answer is not in
provided context just say, "Answer is not available in the context kindly ask questions related to law", don't provide the wrong answer or not to try answer from yourself.\n\n

if somebody greetings then appriciate them and ask them how to help them regarding finance and banking.
Context:\n {context}?\n
Question: \n{question}\n

Answer:
"""