from vec_database import VectorDatabase
from chunking import text_splitter
from generation import chat_groq
from retrieval import insert_to_vecdb, retrieve

prompt_template = """
You are a Rag system, you are to strictly answer QUESTION based on the provided CONTEXT. Do not answer question from your general trained data.
You will be provided with the CONTEXT that you will use to answer the question. If answer is not found in CONTEXT, return "Sorry, the question cannot be answered in the provided document" strictly.

QUESTION: {question}
CONTEXT: {context}
"""
with open("test_docs.txt") as f:
    docs = f.read()

db = VectorDatabase()


def rag(query):
    chunks = text_splitter(text=docs)
    insert_to_vecdb(db, chunks=chunks)
    result = retrieve(db, query)
    prompt = prompt_template.format(question = query, context = result)
    final_answer = chat_groq(prompt)
    return final_answer



print(rag("what are the method of data collection in this project"))
