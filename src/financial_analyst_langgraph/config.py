"""Application configuration."""

from dataclasses import dataclass
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]


@dataclass(frozen=True)
class Settings:
    """Runtime settings for the financial analyst app."""

    database_path: Path = PROJECT_ROOT / "data" / "sample_financials.sqlite"


def load_settings() -> Settings:
    """Load app settings.

    For now we keep configuration intentionally small. Later, this function can
    read `.env` values such as OpenAI and Alpha Vantage API keys.
    """

    return Settings()
