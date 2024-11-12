import os
from pydantic import BaseModel, Field
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

api_key = os.getenv("API_KEY")

class Recipe(BaseModel):
  ingredients: list[str] = Field(description="List of ingredients")
  steps: list[str] = Field(description="List of steps")

def main():
  parser = PydanticOutputParser(pydantic_object=Recipe)

  # LLMの出力の型を指定して、出力をパースする
  format_instructions = parser.get_format_instructions()

  template = """料理のレシピを考えてください。

  {format_instructions}

  料理名: {dish}
  """

  prompt = PromptTemplate(
    template=template,
    invalid_variables=["dish"],
    partial_variables={"format_instructions": format_instructions}
  )

  formatted_prompt = prompt.format_prompt(dish="麻婆豆腐")

  chat = ChatOpenAI(
    model_name="gpt-3.5-turbo-0125",
    temperature=0,
    api_key=api_key)
  messages = [HumanMessage(content=formatted_prompt)]
  output = chat.invoke(messages)
  print(output.content)

if __name__ == '__main__':
  main()
