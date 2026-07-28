import gradio as gr
from sentence_transformers import SentenceTransformer
import sys
from dotenv import load_dotenv
import os

import clickhouse_connect

load_dotenv()

db_host = os.getenv("DATABASE_HOST")
db_user = os.getenv("DATABASE_USER")
db_pass = os.getenv("DATABASE_PASS")
deepseek_token = os.getenv("DEEPSEEK_API_KEY")

model=SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
chclient = clickhouse_connect.get_client(host=db_host,username=db_user,password=db_pass)

# Search query
def search_query(query):
    if not query:
        return "Please enter a search term."
    embeddings = model.encode([query])
    params = {'v1':list(embeddings[0]), 'v2':20}
    result = chclient.query("SELECT id, title, text FROM hackernews ORDER BY cosineDistance(vector, %(v1)s) LIMIT %(v2)s", parameters=params)
    doc_results = ""
    for row in result.result_rows:
        doc_results = doc_results + "\n" + row[2]
    if doc_results!="":
      return doc_results    
    else:
      return "No matches found."


demo = gr.Interface(
    fn=search_query,
    inputs=gr.Textbox(label="Enter search term"),
    outputs=gr.Textbox(label="Search Results"),
    title="Simple Search App",
    description="Type a word to search the local database."
)



if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)