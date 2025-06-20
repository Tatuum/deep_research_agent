from agents import Runner, gen_trace_id,trace
import asyncio
from search_agent import search_agent
from planner_agent import planner_agent, WebSearchList, WebSearchItem
from writer_agent import writer_agent, ReportData
from email_agent import email_agent
#from typing import Dict

class ResearchManager:

    async def run(self, query: str):
        """Run the deep research and yielding the results"""
        trace_id = gen_trace_id()
        with trace("Research Manager", trace_id):
            print("view trace", trace_id=trace_id)
            print(f"View trace: https://platform.openai.com/traces/trace?trace_id={trace_id}")
            yield f"View trace: https://platform.openai.com/traces/trace?trace_id={trace_id}"
            print("Starting research...")
            search_plan = await self.plan_searches(query)
            yield f"Planned {len(search_plan.searches)} searches"
            search_results = await self.perform_searches(search_plan)
            yield f"Performed {len(search_results)} searches"
            report = await self.write_report(query, search_results)
            yield f"Wrote report"
            yield report

    async def plan_searches(self, query: str) -> WebSearchList:
        """Plan the searches for the query"""
        print("Planning searches...")
        result = await Runner.run(
            planner_agent, 
            f"Query: {query}"
            )
        print(f"Planned {len(result.final_output.searches)} searches")
        return result.final_output_as(WebSearchList)
    
    async def search(self, item: WebSearchItem) -> str | None:
        """Search the web for the query"""
        input = f"Search item: {item.query} \nReason for search: {item.reason}"
        try:
            result = await Runner.run(
                search_agent, 
                input
                )
            return str(result.final_output)
        except Exception as e:
            print(f"Error searching for {item.query}: {e}")
            return None

    async def perform_searches(self, search_list: WebSearchList) -> list[str]:
        """Perform the searches for the query"""
        print("Performing searches...")
        tasks = [asyncio.create_task(self.search(item)) for item in search_list.searches]
        results = await asyncio.gather(*tasks)
        return results
    
    async def write_report(self, query: str, search_results: list[str]) -> str:
        """Write the report for the query"""
        print("Writing report...")
        input = f"Original query: {query} \n"
        result = await Runner.run(writer_agent, query, search_results)
        return str(result.final_output)
    
    async def send_email(self, report: ReportData) -> None:
        """Send the report by email"""
        print("Sending email...")
        await Runner.run(email_agent, report.markdown_report)
        return report

