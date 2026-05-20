from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv


load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature= 0
)

def ask_kaya(prompt: str):
    return llm.invoke(prompt).content
