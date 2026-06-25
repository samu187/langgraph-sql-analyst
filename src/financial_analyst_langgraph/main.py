"""Command line entry point for the LangGraph Financial Analyst app."""

from __future__ import annotations

from financial_analyst_langgraph.config import load_settings
from financial_analyst_langgraph.database import get_schema_summary, seed_sample_company


def main() -> None:
    """Run the first CLI version of the app."""

    settings = load_settings()

    print("\nLangGraph Financial Analyst")
    print("===========================")
    print("This first version prepares the database we will use for the LangGraph workflow.\n")

    while True:
        print("Choose a data source:")
        print("1. Use sample company")
        print("2. Select ticker with Alpha Vantage")

        choice = input("\nEnter 1 or 2: ").strip()

        if choice == "1":
            company_id = seed_sample_company(settings.database_path)
            print("\nSample company loaded.")
            print(f"Company ID: {company_id}")
            print(f"Database path: {settings.database_path}")
            print("\nDatabase schema:")
            print(get_schema_summary(settings.database_path))
            print("\nNext step: we will add the LangGraph state and first graph node.")
            return

        if choice == "2":
            print("\nTicker import is not available yet.")
            print("For now, please choose the sample company so we can build the graph together.\n")
            continue

        print("\nPlease enter 1 or 2.\n")


if __name__ == "__main__":
    main()
