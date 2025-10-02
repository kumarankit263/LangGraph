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
class BlogState(TypedDict):
    title: str
    outline: str
    content: str

# 6️⃣ Define the node functions
def create_outline(state:BlogState)->BlogState:

    # fetch title
    title = state['title']

    # call llm gen outline

    prompt=f' Generate a detailed outline for a blog on the topic -{title}'

    outline = model.invoke(prompt).content
    state['outline'] = outline
    return state


def create_blog(state: BlogState) -> BlogState:

    title = state['title']
    outline = state['outline']

    prompt = f'Write a detailed blog on the title - {title} using the follwing outline \n {outline}'

    content = model.invoke(prompt).content

    state['content'] = content

    return state


graph = StateGraph(BlogState)

# nodes
graph.add_node('create_outline', create_outline)
graph.add_node('create_blog', create_blog)

# edges
graph.add_edge(START, 'create_outline')
graph.add_edge('create_outline', 'create_blog')
graph.add_edge('create_blog', END)

workflow = graph.compile()



intial_state = {'title': 'Rise of AI in India'}

final_state = workflow.invoke(intial_state)

print(final_state['content'])