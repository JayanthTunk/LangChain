from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

def generate_bike_name():
    llm = OpenAI(temperature=1) # Temp refers to creativity levels
    name = llm.invoke("Suggest me 5 names for my horse")
    return name

if __name__ == "__main__":
    print(generate_bike_name())