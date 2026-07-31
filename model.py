from langchain_deepseek import ChatDeepSeek
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

def summarize_text(text_to_summarize: str) -> str:

  model = ChatDeepSeek(
    model="deepseek-chat", 
    temperature=0.3,
    max_tokens=500
  )

  prompt = ChatPromptTemplate.from_messages([
        ("system", "You are an expert assistant specialized in text summarization. Your goal is to extract core insights and present them concisely."),
        ("user", "Please provide a brief summary of the following text using bullet points:\n\n{text}")
  ])

  chain = prompt | llm | StrOutputParser()

  response = chain.invoke({"text": text_to_summarize})
  return response

