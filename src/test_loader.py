from data_loader import load_trading_metrics

df = load_trading_metrics()

print(df.head())
print("\nRows loaded:", len(df))
print("\nColumns:")
print(df.columns.tolist())