from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv

load_dotenv()

def generate_bike_name(Animal_type, Animal_colour):
    llm = OpenAI(temperature=1) # Temp refers to creativity levels
    prompt_templates = PromptTemplate(
        input_variables= ["Animal_type", "Animal_colour"],
        template="Suggest me 5 names for my {Animal_type} it is {Animal_colour} in colour"
    ) 
    name_chain = LLMChain(llm =llm, prompt = prompt_templates, output_key ="Animal_names" )
    response = name_chain({'Animal_type': Animal_type, "Animal_colour": Animal_colour})
    return response

if __name__ == "__main__":
    print(generate_bike_name("fish","Golden"))