from pydantic import BaseModel
from agents import Agent

HOW_MANY_SEARCHES = 3

INSTRUCTIONS = f"You are a helpful research assistant. \
    Given a query, come up with a set of web searches to perform to best answer the query. \
     Output {HOW_MANY_SEARCHES} terms to search for."

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
    instructions=INSTRUCTIONS,
    model="gpt-4o-mini",
    output_type=WebSearchList,
    
)