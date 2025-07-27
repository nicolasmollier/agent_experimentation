from dotenv import load_dotenv
import os

from langchain_experimental.graph_transformers import LLMGraphTransformer
from langchain_openai import ChatOpenAI
from langchain_core.documents import Document


load_dotenv(".env")

llm = ChatOpenAI(temperature=0, model_name="gpt-4o")

llm_transformer = LLMGraphTransformer(llm=llm)


text = """
Marie Curie, born in 1867, was a Polish and naturalised-French physicist and chemist who conducted pioneering research on radioactivity.
She was the first woman to win a Nobel Prize, the first person to win a Nobel Prize twice, and the only person to win a Nobel Prize in two scientific fields.
Her husband, Pierre Curie, was a co-winner of her first Nobel Prize, making them the first-ever married couple to win the Nobel Prize and launching the Curie family legacy of five Nobel Prizes.
She was, in 1906, the first woman to become a professor at the University of Paris.
"""
documents = [Document(page_content=text)]
graph_documents = llm_transformer.convert_to_graph_documents(documents)

print(f"Nodes:{graph_documents[0].nodes}")
print(f"Relationships:{graph_documents[0].relationships}")


from langchain_neo4j import Neo4jGraph

graph = Neo4jGraph(
    #url=os.environ["NEO4J_URI"], # "bolt://54.87.130.140:7687",
    #username=os.environ["NEO4J_USERNAME"],
    #database="agentexperimentationdb",
    #password=os.environ["NEO4J_PASSWORD"],
    #refresh_schema=False
)

graph.add_graph_documents(graph_documents)