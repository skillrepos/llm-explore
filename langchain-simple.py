# simple example of using ollama to run local llm
# commands to setup
# curl -fsSL https://ollama.com/install.sh | sh - to install ollama
# ollama serve & - to start ollama
# ollama pull llama2 - to get the llama2 llm
# python langchain-simple.py

from langchain.llms import Ollama

input = input("What is your question?")
llm = Ollama(model="llama2")
res = llm.predict(input)
print (res)