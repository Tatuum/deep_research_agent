# Deep Research Agent (OpenAI SDK, SendGrid, Gradio)

An intelligent research automation system that uses multiple AI agents to perform comprehensive web research, generate detailed reports, and deliver results via email.

## Overview

The Deep Research Agent is a multi-agent system that automates the entire research process:

1. **Planner Agent**: Analyzes your query and creates a strategic search plan
2. **Search Agent**: Performs web searches and summarizes findings
3. **Writer Agent**: Synthesizes research into comprehensive reports
4. **Email Agent**: Delivers final reports via email

The system provides both a web interface (Gradio) and programmatic access for research automation.

## Quick Start

### Prerequisites

- Python 3.12 or higher
- UV package manager
- OpenAI API key
- SendGrid API key (for email functionality)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd deep_research_agent
   ```

2. **Install UV (if not already installed)**
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

3. **Install dependencies using UV**
   ```bash
   uv sync
   ```

4. **Activate the virtual environment**
   ```bash
   source .venv/bin/activate  # On Unix/macOS
   # or
   .venv\Scripts\activate     # On Windows
   ```

5. **Set up environment variables**
   Create a `.env` file in the project root:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   SENDGRID_API_KEY=your_sendgrid_api_key_here
   ```

6. **Launch the web interface**
   ```bash
   python deep_research.py
   ```

7. **Open your browser** and navigate to the provided URL (typically `http://localhost:7860`)

## Usage

### Web Interface

1. Enter your research query in the text box
2. Click "Run" to start the research process
3. Watch real-time progress updates
4. Receive the final report via email

## Architecture

### Agent Components

- **`planner_agent.py`**: Creates strategic search plans based on queries
- **`search_agent.py`**: Performs web searches and summarizes results
- **`writer_agent.py`**: Synthesizes research into comprehensive reports
- **`email_agent.py`**: Handles email delivery of final reports
- **`research_manager.py`**: Orchestrates the entire research workflow

### Configuration

- **`config.py`**: Centralized configuration for agent instructions and settings
- **`deep_research.py`**: Gradio web interface
- **`main.py`**: Simple entry point

## Configuration

### Search Settings

In `config.py`, you can customize:
- Number of searches per query (`HOW_MANY_SEARCHES`)
- Agent instructions for each component
- Email settings

### Email Configuration

Update email settings in `email_agent.py`:
```python
from_email = Email("your-email@domain.com")
to_email = To("recipient@domain.com")
```

## Dependencies

- **gradio**: Web interface framework
- **openai**: OpenAI API integration
- **openai-agents**: Agent framework
- **python-dotenv**: Environment variable management
- **sendgrid**: Email delivery service
- **pydantic**: Data validation and serialization

## Development

### Project Structure

```
deep_research_agent/
├── planner_agent.py        # Agent implementations
├── search_agent.py         # Agent implementations
├── writer_agent.py         # Agent implementations
|── email_agent.py          # Agent implementations
├── research_manager.py     # Main orchestration
├── deep_research.py        # Web interface
├── config.py              # Configuration
├── main.py                # Entry point
├── pyproject.toml         # Project metadata

```

## Troubleshooting

### Common Issues

1. **API Key Errors**: Ensure your OpenAI and SendGrid API keys are correctly set in `.env`
2. **Import Errors**: Make sure all dependencies are installed with `uv sync`
3. **Email Delivery**: Check SendGrid API key and email configuration

### Debugging

The system provides OpenAI traces for debugging:
- Trace URLs are displayed in the console output
- Visit the trace URL to see detailed agent interactions



**Note**: This project requires valid API keys for OpenAI and SendGrid to function properly. Make sure to set up your environment variables before running the application.
