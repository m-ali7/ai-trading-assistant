from data_loader import load_trading_metrics
from manager_brief_generator import generate_manager_brief

df = load_trading_metrics()

brief = generate_manager_brief(
    df,
    manager_email="sarah.trader@retailer.com"
)

print(brief)