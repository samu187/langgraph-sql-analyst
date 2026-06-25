# LangGraph Financial Analyst

A Python portfolio project that uses LangGraph, SQLite, and OpenAI to answer natural-language questions about financial statements.

The assistant can work with bundled sample data or, in a later version, fetch company financial statements from Alpha Vantage when the user provides an API key and ticker symbol.

## Project Goals

- Teach LangGraph step by step through a practical automation project.
- Convert natural-language finance questions into safe SQL queries.
- Inspect database schema before querying.
- Validate that generated SQL is read-only.
- Calculate financial metrics such as revenue growth, margins, liquidity ratios, and free cash flow.
- Return structured responses that can later be rendered as text, tables, bar charts, or line charts.

## Planned Workflow

```text
User question
   -> classify intent
   -> inspect database schema
   -> plan analysis
   -> generate SQL
   -> validate SQL safety
   -> execute SQL
   -> calculate metrics
   -> choose response format
   -> produce final answer
```

## Tech Stack

- Python
- LangGraph
- LangChain
- OpenAI API
- SQLite
- Rich or Textual for an initial terminal interface
- Streamlit or React/FastAPI for a later visual frontend

## Project Structure

```text
.
├── data/
│   └── .gitkeep
├── docs/
│   └── .gitkeep
├── scripts/
│   ├── .gitkeep
│   └── seed_sample_data.py
├── src/
│   └── financial_analyst_langgraph/
│       ├── __init__.py
│       ├── __main__.py
│       ├── config.py
│       ├── database.py
│       └── main.py
├── tests/
│   └── .gitkeep
├── .env.example
├── .gitignore
├── pyproject.toml
└── README.md
```

## Setup

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the project in editable mode:

```bash
pip install -e ".[dev]"
```

Create a local environment file:

```bash
cp .env.example .env
```

Then add your OpenAI API key to `.env`:

```bash
OPENAI_API_KEY=your_openai_api_key_here
```

Alpha Vantage support is planned as an optional data source:

```bash
ALPHA_VANTAGE_API_KEY=your_alpha_vantage_key_here
```

## Development Notes

This repository is being built as a learning project. The first version will focus on the LangGraph workflow and a local SQLite sample database. Once the graph is stable, a frontend can render the graph's structured output as text, tables, and charts.

## Run The App

During early development, run the app with the `src` folder on the Python path:

```bash
PYTHONPATH=src python3 -m financial_analyst_langgraph
```

Then choose:

```text
1. Use sample company
```

The app will create:

```text
data/sample_financials.sqlite
```

You can also seed the sample database directly:

```bash
PYTHONPATH=src python3 scripts/seed_sample_data.py
```

The sample database contains five years of annual data across:

- `companies`
- `income_statements`
- `balance_sheets`
- `cash_flow_statements`

For the cash flow statement:

```text
change_in_cash = operating_cash_flow + investing_cash_flow + financing_cash_flow
free_cash_flow = operating_cash_flow + capex
```

In this project, `capex` is stored as a negative cash outflow.

## Git Quick Start

Check the repository status:

```bash
git status
```

Stage files:

```bash
git add .
```

Create a commit:

```bash
git commit -m "Initial project scaffold"
```

View commit history:

```bash
git log --oneline
```
