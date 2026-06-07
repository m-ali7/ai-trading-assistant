from data_loader import load_trading_metrics
from analysis_engine import analyse_category
from root_cause_engine import identify_root_cause
from recommendation_engine import recommend_actions

df = load_trading_metrics()

analysis = analyse_category(
    df,
    market="UK",
    category="Womenswear"
)

root_cause = identify_root_cause(analysis)

recommendations = recommend_actions(root_cause)

print("Analysis:")
print(analysis)

print("\nRoot Cause:")
print(root_cause)

print("\nRecommendations:")
print(recommendations)