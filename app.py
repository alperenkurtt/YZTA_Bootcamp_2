import streamlit as st

from llm_client import get_response
from prompts import SYSTEM_PROMPT

st.set_page_config(page_title="Fluentie", page_icon="🗣️")
st.title("Fluentie")

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": SYSTEM_PROMPT}]

for message in st.session_state.messages:
    if message["role"] == "system":
        continue
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if user_input := st.chat_input("Type a message in English..."):
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        try:
            reply = get_response(st.session_state.messages)
        except Exception as e:
            reply = f"Bir hata oluştu: {e}"
        st.markdown(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})
