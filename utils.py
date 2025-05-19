from langchain.chains import ConversationChain
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
import os

def get_chat_response(prompt, memory, ai_api_key):
    model = ChatOpenAI(model = "deepseek-chat",openai_api_key=ai_api_key,openai_api_base = "https://api.deepseek.com")
    chain = ConversationChain(llm = model,memory = memory)

    response = chain.invoke({"input":prompt})
    return response["response"]

# memory_0 = ConversationBufferMemory(return_messages = True)
# print(get_chat_response("牛顿提出过哪些知名理论？",memory_0,os.getenv("DEEPSEEK_API_KEY")))
# print(get_chat_response("我上个问题问的是什么？",memory_0,os.getenv("DEEPSEEK_API_KEY")))