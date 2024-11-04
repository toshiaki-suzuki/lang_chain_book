import os
from langchain_openai import ChatOpenAI
from langchain_core.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

api_key = os.getenv("API_KEY")

def main():
  chat = ChatOpenAI(
    model_name="gpt-3.5-turbo-0125",
    temperature=0,
    streaming=True,
    callbacks=[StreamingStdOutCallbackHandler()],
    api_key=api_key)

  messages = [
    HumanMessage(content="自己紹介をしてください。"),
  ]

  # invokeメソッドを使う
  result = chat.invoke(messages)
  print(result.content)

if __name__ == '__main__':
    main()
