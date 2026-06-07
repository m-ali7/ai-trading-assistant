from src.analysis_engine import analyse_category
from src.root_cause_engine import identify_root_cause
from src.recommendation_engine import recommend_actions
from src.llm_commentary_generator import generate_llm_commentary


def answer_trading_question(df, market: str, category: str, question: str) -> str:
    """
    Answers an ad-hoc trading question using the same grounded analysis chain
    as the Monday brief.
    """

    analysis = analyse_category(df, market, category)
    root_cause = identify_root_cause(analysis)
    recommendations = recommend_actions(root_cause)

    response = generate_llm_commentary(
        analysis,
        root_cause,
        recommendations
    )

    return f"""
QUESTION
--------
{question}

ANSWER
------
{response}
"""