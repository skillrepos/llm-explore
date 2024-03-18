#importing the main libraries for setting up code to interact with LLM
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.prompts import PromptTemplate
from langchain_community.llms import LlamaCpp

# Defining a Promt Template to interact with LLM
template = """Question: {question}
Answer: Let’s work this out in a step by step way to be sure we have the right answer."""

# Callbacks support token-wise streaming
callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])
n_gpu_layers = 1 # Change this value based on your model and your GPU VRAM pool.
n_batch = 512 # Should be between 1 and n_ctx, consider the amount of VRAM in your GPU.

# Make sure the model path is correct for your system!
llm = LlamaCpp(
model_path="/home/vscode/.cache/lm-studio/models/TheBloke/Llama-2-7B-Chat-GGUF/llama-2-7b-chat.Q4_K_S.gguf",
n_gpu_layers=n_gpu_layers, n_batch=n_batch,
n_ctx = 3000,
temperature=0.0,
max_tokens=2000,
top_p=1,
callback_manager=callback_manager,
verbose=True, # Verbose is required to pass to the callback manager
)
#Question for LLM
question = "Which are the top 5 companies in world with their revenue in table format?"

#providing the results
print("<====================================== Outcome from model =======================================>")
llm.invoke(question)
