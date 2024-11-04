import os
# from langchain.llms import OpenAI は deprecated
from langchain_openai import OpenAI

api_key = os.getenv("API_KEY")

def main():
  llm = OpenAI(
    model_name="davinci-002",
    temperature=0,
    api_key=api_key)

  # invokeメソッドを使う
  result = llm.invoke('自己紹介してください。')
  print(result)

if __name__ == '__main__':
    main()
