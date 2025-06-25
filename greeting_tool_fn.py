from langchain.tools import Tool

def greeting_tool_fn(_:str) -> str:
    return "Helloo! Im your assistant. How can i help you today :)?"

greeting_tool = Tool(
    name="Greeting Tool",
    func=greeting_tool_fn,
    description="Use this tool to greet users who say hi or hello."
)



