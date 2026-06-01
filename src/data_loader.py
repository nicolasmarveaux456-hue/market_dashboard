from pathlib import Path
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"


def load_prices():
    """
    Load monthly prices from the data folder.
    """
    return pd.read_csv(DATA_DIR / "monthly_prices.csv",index_col=0,parse_dates=True)


def load_returns():
    """
    Load monthly returns from the data folder.
    """
    return pd.read_csv(DATA_DIR / "monthly_returns.csv",index_col=0,parse_dates=True)


def load_backtest_summary():
    """
    Load backtest results containing strategy and benchmark equity curves.
    """
    return pd.read_csv(DATA_DIR / "backtest_summary.csv",index_col=0,parse_dates=True)


def load_performance_metrics():
    """
    Load performance metrics for the strategy and benchmark.
    """
    return pd.read_csv(DATA_DIR / "performance_metrics.csv",index_col=0)