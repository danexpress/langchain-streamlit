from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType

from dotenv import load_dotenv

load_dotenv()


def generate_expensive_breed(animal_type, price_point):
    llm = OpenAI(temperature=0.7)

    prompt_template_name = PromptTemplate(
        input_variables=["animal_type", "price_point"],
        template="Name five best breeds of {animal_type} i can get at {price_point}.",
    )

    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="pet_name")

    response = name_chain({"animal_type": animal_type, "price_point": price_point})
    return response


def langchain_agent():
    llm = OpenAI(temperature=0.5)

    tools = load_tools(["wikipedia", "llm-math"], llm=llm)

    agent = initialize_agent(
        tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
    )

    result = agent.run("What is the average age of a dog? Multiply the age by 2")

    print(result)


if __name__ == "__main__":
    langchain_agent()
    # print(generate_expensive_breed("dog", "five thousand dollars"))
