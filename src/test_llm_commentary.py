from data_loader import load_trading_metrics
from analysis_engine import analyse_category
from root_cause_engine import identify_root_cause
from recommendation_engine import recommend_actions
from llm_commentary_generator import generate_llm_commentary

df = load_trading_metrics()

analysis = analyse_category(
    df,
    market="UK",
    category="Womenswear"
)

root_cause = identify_root_cause(analysis)
recommendations = recommend_actions(root_cause)

brief = generate_llm_commentary(
    analysis,
    root_cause,
    recommendations
)

print(brief)