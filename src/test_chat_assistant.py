from data_loader import load_trading_metrics
from chat_assistant import answer_trading_question

df = load_trading_metrics()

answer = answer_trading_question(
    df,
    market="UK",
    category="Dresses",
    question="Why did UK Dresses decline last week?"
)

print(answer)