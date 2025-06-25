from langchain.tools import Tool

def bodmas_tool_fn(expression: str) -> str:
    try:
        result = eval(expression, {"__builtins__": {}}, {})
        return f"The result of '{expression}' is {result}"
    except Exception as e:
        return f"Error evaluating expression: {str(e)}"

bodmas_tool = Tool(
    name="BODMAS Tool",
    func=bodmas_tool_fn,
    description="Use this tool to solve math expressions using BODMAS. Example: 2+3*4"
)