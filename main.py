from dotenv import load_dotenv
load_dotenv()

# from langchain_openai import OpenAI
# llm = OpenAI()
# llm_response = llm.invoke("안녕!")
# print(llm_response)


from langchain_openai import ChatOpenAI
chat_model = ChatOpenAI()
chat_response = chat_model.invoke("나도 아무거나 잘 먹어. 지금 나이가 들어서 많이 못먹어. 그래서 맛있는거 먹고싶어.")
# print(chat_response)
print(chat_response.content)


