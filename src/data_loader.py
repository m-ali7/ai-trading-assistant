import pandas as pd


def load_trading_metrics(file_path: str = "data/trading_metrics.csv") -> pd.DataFrame:
    """
    Loads trading metrics from the prototype CSV file.

    In this prototype, the CSV represents the retailer's existing APIs/connectors.
    In production, this function would be replaced by real API calls.
    """
    return pd.read_csv(file_path)