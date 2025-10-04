import os
from dotenv import load_dotenv

# 1️⃣ Load .env
load_dotenv()

# 2️⃣ Set API key BEFORE importing Gemini classes
os.environ["GOOGLE_API_KEY"] = os.getenv("API_KEY")

# 3️⃣ Now import Gemini model
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import StateGraph,START, END
from typing import TypedDict, Literal, Annotated
from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.graph.message import add_messages

# 4️⃣ Initialize Gemini model
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

class ChatState(TypedDict):
    messages:Annotated[list[BaseMessage],add_messages]

def chat_node(state:ChatState):

    messages=state["messages"]

    response=llm.invoke(messages)

    return {'messages':[response]}


graph = StateGraph(ChatState)

# add nodes
graph.add_node('chat_node', chat_node)

graph.add_edge(START, 'chat_node')
graph.add_edge('chat_node', END)

chatbot = graph.compile()


# initial_state = {
#     'messages': [HumanMessage(content='What is the capital of Bihar')]
# }

# result=chatbot.invoke(initial_state)['messages'][-1].content
# print(result)


while True:

    user_message=input("Type here: ")
    print("You:",user_message)

    if  user_message.strip().lower() in ["exit", "quit", "bye"]:
        print("Bot: Goodbye!")
        break
    response=chatbot.invoke(
        {
            'messages':[HumanMessage(content=user_message)]
        }
    )

    bot_message=response['messages'][-1].content
    print('Bot:',bot_message)
                          



