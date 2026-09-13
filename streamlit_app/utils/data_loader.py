from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[2]
PROCESSED_DIR = ROOT / "data" / "processed"


def load_mart(name: str) -> pd.DataFrame:
    """Load a processed analytical mart from Parquet."""
    path = PROCESSED_DIR / f"{name}.parquet"

    if not path.exists():
        raise FileNotFoundError(
            f"Processed mart not found: {path}"
        )

    return pd.read_parquet(path)


def load_daily_growth() -> pd.DataFrame:
    """Load daily product growth metrics."""
    return load_mart("mart_product_growth_daily")


def load_cohort_retention() -> pd.DataFrame:
    """Load cohort retention metrics."""
    return load_mart("mart_cohort_retention")


def load_experiment_results() -> pd.DataFrame:
    """Load experiment results."""
    return load_mart("mart_experiment_results")