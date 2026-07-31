import gradio as gr
from sentence_transformers import SentenceTransformer
import sys
from dotenv import load_dotenv
import os

import clickhouse_connect
from model import summarize_text

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
    doc_results = []
    for row in result.result_rows:
        doc_results.append(row[2])
    if len(doc_results)>0:
      text_to_sum="\n".join(doc_results)
      return summarize_text(text_to_sum),doc_results    
    else:
      return "",doc_results

with gr.Blocks(title="Hackernews Search App") as demo:
   with gr.Column():
        in_box = gr.Textbox(label="Enter search term")
        btn = gr.Button("Search")
        out_text = gr.Textbox(label="Search summary")
        out_table=gr.Dataframe(label="Search Results")
        btn.click(fn=search_query, inputs=in_box, outputs=[out_text,out_table])


if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)