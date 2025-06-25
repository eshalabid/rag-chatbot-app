from langchain.tools import Tool

def web_search_tool(query:str) -> str:
    eb_links = {
        "linkedin": "https://www.linkedin.com",
        "github": "https://www.github.com",
        "stackoverflow": "https://stackoverflow.com",
        "openai": "https://www.openai.com",
        "youtube": "https://www.youtube.com",
    }
    query_lower = query.lower()
    for name, link in eb_links.items():
        if name in query_lower:
            return f"Here’s the link to {name.title()}: {link}"
    return "Sorry, I couldn’t find a matching website in my list."

web_tool = Tool(
    name="Web Tool",
    func=web_search_tool,
    description="Use this tool to provide links to websites like GitHub, LinkedIn, etc."
)
