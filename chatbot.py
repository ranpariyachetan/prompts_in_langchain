from langchain_openai import ChatOpenAI
from dotenv import  load_dotenv
from langchain_core.prompts import  PromptTemplate, load_prompt


load_dotenv()

model = ChatOpenAI(model="gpt-4")

chat_history = []

while True:
    user_input = input("You: ")
    chat_history.append(user_input)
    if user_input == "exit":
        break

    result = model.invoke(chat_history)
    chat_history.append(result.content)
    print(f"AI: {result.content}")

print(chat_history)