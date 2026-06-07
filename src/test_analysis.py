from data_loader import load_trading_metrics
from analysis_engine import analyse_category

df = load_trading_metrics()

results = analyse_category(
    df,
    market="UK",
    category="Womenswear"
)

print(results)