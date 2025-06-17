from pydantic import BaseModel
from agents import Agent
from config import INSTRUCTIONS_PLANNER


class WebSearchItem(BaseModel):
    reason: str
    "Your reasoning why this search is relevant to the query"

    query: str
    "The actual search term"

class WebSearchList(BaseModel):
    searches: list[WebSearchItem]
    "A list of web searches to perform"

planner_agent = Agent(
    name="Web Search Planner",
    instructions=INSTRUCTIONS_PLANNER,
    model="gpt-4o-mini",
    output_type=WebSearchList,
    
)