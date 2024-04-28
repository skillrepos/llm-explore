# use this for lab
# simple example of using llamaindex and ollama to work with documents
# create ./documents folder and put any desired pdfs in it
# curl -fsSL https://ollama.com/install.sh | sh 
# ollama serve & 
# ollama pull llama2 
# streamlit run rag-chat.py
import streamlit as st
import os
import os.path

from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, load_index_from_storage, ServiceContext, StorageContext
from llama_index.core.response.pprint_utils import pprint_response
from langchain_community.llms import Ollama

from llama_index.embeddings.huggingface import HuggingFaceEmbedding

storage_path = "./vectorstore"
documents_path = "./documents"
llm = Ollama(model="llama2")
embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")

from llama_index.core import Settings

Settings.llm = llm
Settings.embed_model = embed_model
Settings.chunk_size = 512
Settings.chunk_overlap = 64


Settings.embed_model = embed_model

@st.cache_resource(show_spinner=False)
def initialize(): 
    if not os.path.exists(storage_path):
        documents = SimpleDirectoryReader(documents_path).load_data()
        index = VectorStoreIndex.from_documents(documents)
        index.storage_context.persist(persist_dir=storage_path)
    else:
        storage_context = StorageContext.from_defaults(persist_dir=storage_path)
        index = load_index_from_storage(storage_context)
    return index
index = initialize()

st.title("Ask the Document")
if "messages" not in st.session_state.keys(): 
    st.session_state.messages = [
        {"role": "assistant", "content": "Ask me a question !"}
    ]

chat_engine = index.as_chat_engine(chat_mode="condense_question", verbose=True)

if prompt := st.chat_input("Your question"): 
    st.session_state.messages.append({"role": "user", "content": prompt})

for message in st.session_state.messages: 
    with st.chat_message(message["role"]):
        st.write(message["content"])
        
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = chat_engine.chat(prompt)
            st.write(response.response)
            pprint_response(response, show_source=True)
            message = {"role": "assistant", "content": response.response}
            st.session_state.messages.append(message) 