import os
from langchain.prompts import ChatPromptTemplate, PromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain_core.messages import HumanMessage, SystemMessage

api_key = os.getenv("API_KEY")

template = """
以下の料理のレシピを考えてください。

料理名: {dish}
"""

def main():
  chat_prompt = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(" あなたは{country}料理のプロフェッショナルです。"),
    HumanMessagePromptTemplate.from_template(" 以下の料理のレシピを考えてください。 \n\n料理名: {dish} "),
  ])

  messages = chat_prompt.format_prompt(country="中華", dish="麻婆豆腐").to_messages()
  print(messages)

if __name__ == '__main__':
    main()
