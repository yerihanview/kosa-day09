from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
chat_model = ChatOpenAI()

# subject = "당근"

# chat_response = chat_model.invoke(subject+"에 대해 설명해줘.")
# print(chat_response.content)

import streamlit as st
import time

st.title("디지털 글쓰기"+ chat_model.model)
subject = st.text_input("글 쓸 주제를 입력해주세요.")

if st.button("궁금증 해결해줘~", type="primary", icon="🔍"):
    with st.spinner("Wait for it...", show_time=True):
        chat_response = chat_model.invoke(subject+"에 대해 설명해줘.")
        st.write(chat_response.content)


