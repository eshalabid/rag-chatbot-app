from langchain.agents import initialize_agent, AgentType
from tools.tool import tools
from llm.llm_provider import llm

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

if __name__ == "__main__":
    query = "linux file permissions?"
    response = agent.invoke({"input": query})
    print("\n🤖 Agent's Answer:\n", response.get("output"))