from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType

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


def langchain_agent(): 
    llm = OpenAI(temperature= 0.5)
    tools = load_tools(["wikipedia", "llm-math"],llm=llm)
    agent = initialize_agent(
        tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose = True 
    )


    result = agent.run(
        "What is the average age of a cat? Multiply the age by 3"
    )

if __name__ == "__main__":
    langchain_agent()
    #print(generate_bike_name("fish","Golden"))