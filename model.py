from langchain_deepseek import ChatDeepSeek
from langchain_core.prompts import ChatPromptTemplate
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import ReduceDocumentsChain, MapReduceDocumentsChain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.documents import Document

model = ChatDeepSeek(
    model="deepseek-chat", 
    temperature=0.3
)