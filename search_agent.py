from agents import Agent, WebSearchTool, ModelSettings
from config import INSTRUCTIONS_SEARCH

search_agent = Agent(
    name="Search Agent",
    instructions=INSTRUCTIONS_SEARCH,
    tools=[WebSearchTool(search_context_size="low")],
    model="gpt-4o-mini",
    model_settings=ModelSettings(tool_choice="required")
)