import os
from dotenv import load_dotenv

# 1️⃣ Load .env
load_dotenv()

# 2️⃣ Set API key BEFORE importing Gemini classes
os.environ["GOOGLE_API_KEY"] = os.getenv("API_KEY")

# 3️⃣ Now import Gemini model
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import StateGraph, START, END
from typing import TypedDict

# 4️⃣ Initialize Gemini model
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# 5️⃣ Define your state
class LLMState(TypedDict):
    question: str
    answer: str

# 6️⃣ Define the node function
def llm_qa(state: LLMState) -> LLMState:
    question = state['question']
    prompt = f"Answer the following question: {question}"
    
    # Ask Gemini
    answer = model.invoke(prompt).content
    state['answer'] = answer
    return state

# 7️⃣ Create the LangGraph workflow
graph = StateGraph(LLMState)
graph.add_node('llm_qa', llm_qa)
graph.add_edge(START, 'llm_qa')
graph.add_edge('llm_qa', END)

workflow = graph.compile()

# 8️⃣ Execute
initial_state = {'question': 'How far is the moon from the earth?'}
final_state = workflow.invoke(initial_state)

print(final_state['answer'])
