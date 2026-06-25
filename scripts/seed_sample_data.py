"""Seed the local SQLite database with bundled sample financial statements."""

from financial_analyst_langgraph.config import load_settings
from financial_analyst_langgraph.database import seed_sample_company


def main() -> None:
    settings = load_settings()
    company_id = seed_sample_company(settings.database_path)
    print(f"Seeded sample company with id {company_id}.")
    print(f"Database path: {settings.database_path}")


if __name__ == "__main__":
    main()
