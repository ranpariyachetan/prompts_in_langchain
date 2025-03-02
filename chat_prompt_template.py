from langchain_core.prompts import ChatPromptTemplate

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

chat_template = ChatPromptTemplate([
    ("system", "You are a helpful {domain} expert."),
    ("human", "Explain in simple terms, what is {topic}.")
])

prompt = chat_template.invoke({"domain": "cricket", "topic": "Dusra"})

print(prompt)