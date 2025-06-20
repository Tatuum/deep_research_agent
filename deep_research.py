import gradio as gr
from dotenv import load_dotenv
from research_manager import ResearchManager

load_dotenv()

async def run(query: str):
    async for chunk in ResearchManager().run(query):
        yield chunk

with gr.Blocks() as demo:
    gr.Markdown("Deep Research")
    query = gr.Textbox(label="Query")
    run_button = gr.Button("Run")
    output = gr.Markdown(label="Output")

    run_button.click(fn=run, inputs=query, outputs=output)

demo.launch()