import os
from langchain.prompts import PromptTemplate

api_key = os.getenv("API_KEY")

template = """
以下の料理のレシピを考えてください。

料理名: {dish}
"""

def main():
  prompt = PromptTemplate(
    input_variables=["dish"],
    template=template,
    api_key=api_key)
  result = prompt.format(dish="カレーライス")
  print(result)

if __name__ == '__main__':
    main()
