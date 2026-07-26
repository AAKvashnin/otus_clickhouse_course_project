import gradio as gr
from sentence_transformers import SentenceTransformer
import sys


import clickhouse_connect

# Search query
def search_query(query):
    return "No matches found."


demo = gr.Interface(
    fn=search_query,
    inputs=gr.Textbox(label="Enter search term"),
    outputs=gr.Textbox(label="Search Results"),
    title="Simple Search App",
    description="Type a word to search the local database."
)

model=SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

chclient = clickhouse_connect.get_client() #


if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)