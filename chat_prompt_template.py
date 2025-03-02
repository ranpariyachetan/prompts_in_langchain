from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

chat_template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful {domain} expert."),
    ("human", "Explain in simple terms, what is {topic}.")
])

prompt = chat_template.invoke({"domain": "cricket", "topic": "Dusra"})

print(prompt)