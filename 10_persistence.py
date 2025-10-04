import os
from dotenv import load_dotenv

# 1️⃣ Load .env
load_dotenv()

# 2️⃣ Set API key BEFORE importing Gemini classes
os.environ["GOOGLE_API_KEY"] = os.getenv("API_KEY")

# 3️⃣ Now import Gemini model
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import StateGraph,START, END
from typing import TypedDict
from langgraph.checkpoint.memory import InMemorySaver

# 4️⃣ Initialize Gemini model
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

class JokeState(TypedDict):
    topic:str
    joke:str
    explanation:str

def generate_joke(state:JokeState):

    prompt=f"generate a joke on the topic {state['topic']}"
    response=llm.invoke(prompt).content

    return {"joke":response}

def generate_explaination(state:JokeState):

    prompt =f"write an explaination for the joke -{state['joke']}"
    response=llm.invoke(prompt).content
    return {"explanation":response}

graph=StateGraph(JokeState)
graph.add_node('generate_joke', generate_joke)
graph.add_node('generate_explaination', generate_explaination)

# edges
graph.add_edge(START, 'generate_joke')
graph.add_edge('generate_joke', 'generate_explaination')
graph.add_edge('generate_explaination', END)

# checkpointing
checkpointer=InMemorySaver()
workflow=graph.compile(checkpointer=checkpointer)


config1 = {"configurable": {"thread_id": "1"}}
result=workflow.invoke({'topic':'pizza'}, config=config1)

# result1=workflow.get_state(config1)
# print(result1)

# result2=list(workflow.get_state_history(config1))
# print(result2)


# checkpoint_id': '1f0a1023-faf7-6476-8000-00f2330fdc54'


# TIME TRAVEL           Updating State
result3=workflow.update_state({"configurable": {"thread_id": "1", "checkpoint_id": "1f0a1023-faf7-6476-8000-00f2330fdc54", 
                                                "checkpoint_ns": ""}}, {'topic':'samosa'})


print(result3)

result4=workflow.invoke(None, {"configurable": {"thread_id": "1", "checkpoint_id": "1f0a1023-faf7-6476-8000-00f2330fdc54"}})
print(result4)
