from pydantic import BaseModel
from agents import Agent
from config import INSTRUCTIONS_WRITER



class ReportData(BaseModel):
    short_summary: str
    """A short 2-3 sentence summary of the findings."""

    markdown_report: str
    """The final report"""

    follow_up_questions: list[str]
    """Suggested topics to research further"""

writer_agent = Agent(
    name="WriterAgent",
    instructions=INSTRUCTIONS_WRITER,
    model="gpt-4o-mini",
    output_type=ReportData,
)