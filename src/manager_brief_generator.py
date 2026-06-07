from analysis_engine import analyse_category
from root_cause_engine import identify_root_cause
from recommendation_engine import recommend_actions
from llm_commentary_generator import generate_llm_commentary
from executive_summary_generator import generate_executive_summary


def generate_manager_brief(df, manager_email: str) -> str:
    """
    Generates a personalised Monday brief for one trading manager.
    """

    manager_rows = df[df["manager_email"] == manager_email]

    if manager_rows.empty:
        return f"No trading data found for manager: {manager_email}"

    manager_name = manager_rows.iloc[0]["manager_name"]

    category_results = []

    assignments = manager_rows[["market", "category"]].drop_duplicates()

    for _, row in assignments.iterrows():
        market = row["market"]
        category = row["category"]

        analysis = analyse_category(df, market, category)
        root_cause = identify_root_cause(analysis)
        recommendations = recommend_actions(root_cause)

        commentary = generate_llm_commentary(
            analysis,
            root_cause,
            recommendations
        )

        category_results.append({
            "analysis": analysis,
            "root_cause": root_cause,
            "recommendations": recommendations,
            "commentary": commentary,
        })

    executive_summary = generate_executive_summary(category_results)

    brief = f"""
PERSONALISED MONDAY TRADING BRIEF

Manager: {manager_name}
Email: {manager_email}

========================================

{executive_summary}

========================================
CATEGORY DETAIL
========================================
"""

    for result in category_results:
        analysis = result["analysis"]
        commentary = result["commentary"]

        brief += f"""

----------------------------------------
{analysis['market']} | {analysis['category']}
----------------------------------------

{commentary}

"""

    return brief