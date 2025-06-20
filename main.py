from langchain_core.messages import HumanMessage #Allows us to build AI applications
from langchain_openai import ChatOpenAI    #allows us to use open AI with langchain and langgraph
from langchain.tools import tool 
from langgraph.prebuilt import create_react_agent #Framework that allows us to build an AI agent
from dotenv import load_dotenv   #allows us to load enviorment variable files.



#the difference between an Ai chatbot and Ai agent is that Ai agents have access to tools, this allows AI to respond to more complex responses, like mathmatics
load_dotenv()
@tool #it wont use the tool if it doesnt find it useful
def calculator(a:float,b:float) -> str: 
     """Useful for perrforming basic arthmeric calculations with numbers"""
     print("tool has been called.")
     return f"The sum of {a} and {b} is {a + b}"
def greeting(name:str) -> str:
     """Useful for greeting a user"""
     print("tool has been called.")
     return f"Hello {name}, I hope you are well "

def main():
    model = ChatOpenAI(temperature=0) #the higher the temperature the more random the answers will be
    tools = [calculator, greeting]
    agent_executor = create_react_agent(model, tools)
    print("Welcome! I'm your AI Assistant. Type 'quit' to exit.")
    print("You can ask me to perform calculations or chat with me.")

    while True:
        user_input = input("\nYou: ").strip()
        if user_input == "quit":
            break
        print("\nAssistant: ", end = "")
        for chunk in agent_executor.stream(
            {"messages": [HumanMessage(content=user_input)]}
        ):
            if "agent" in chunk and "messages" in chunk["agent"]:
                for message in chunk["agent"]["messages"]:
                        print(message.content, end="")
        print()
if __name__ == "__main__":  #this is how to execute a main function in python
     main()


