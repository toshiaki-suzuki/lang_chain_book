import os
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

api_key = os.getenv("API_KEY")

def main():
  chat = ChatOpenAI(
    model_name="gpt-3.5-turbo-0125",
    temperature=0,
    api_key=api_key)

  messages = [
    SystemMessage(content="You're a helpful assistant"),
    HumanMessage(content="私はジャギといいます。"),
    AIMessage(content="こんにちは、ジャギさん。どのようなお手伝いができますか？"),
    HumanMessage(content="俺の名を言ってみろ。"),
  ]

  # invokeメソッドを使う
  result = chat.invoke(messages)
  print(result.content)

if __name__ == '__main__':
    main()
