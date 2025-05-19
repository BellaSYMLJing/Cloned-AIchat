import streamlit as st
from langchain.memory import ConversationBufferMemory

from utils import get_chat_response

st.title("💬克隆AI对话助手")

with st.sidebar:
    deepseek_api_key = st.text_input("请输入DeepSeek API密钥：",type="password")
    st.markdown("[获取DeepSeek API密钥](https://platform.deepseek.com/api_keys)")

if "memory" not in st.session_state:
    st.session_state["memory"] = ConversationBufferMemory(return_messages=True)
    st.session_state["messages"] = [{"role":"ai",
                                     "content":"你好，我是你的AI助手，请问有什么可以帮你？😊"}]

for message in st.session_state["messages"]:
    st.chat_message(message["role"]).write(message["content"])

prompt = st.chat_input()
if prompt:
    if not deepseek_api_key:
        st.info("请输入你的DeepSeek API Key")
        st.stop()
    st.session_state["messages"].append({"role":"human","content":prompt})
    st.chat_message("human").write(prompt)

    with st.spinner("AI正在努力思考中🤔️，请稍等..."):
        response = get_chat_response(prompt,st.session_state["memory"],deepseek_api_key)

    msg = {"role":"ai","content":response}
    st.session_state["messages"].append(msg)
    st.chat_message("ai").write(response)