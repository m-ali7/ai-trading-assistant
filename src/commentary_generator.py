def generate_commentary(
    analysis: dict,
    root_cause: dict,
    recommendations: dict
) -> str:

    commentary = f"""
WEEKLY TRADING BRIEF

Market: {analysis['market']}
Category: {analysis['category']}

Headline Metrics
----------------
Revenue Change: {analysis['revenue_change_pct']:.2f}%
Traffic Change: {analysis['traffic_change_pct']:.2f}%
Conversion Change: {analysis['conversion_change_pct']:.2f}%
Margin Change: {analysis['margin_change_pct']:.2f}%

Root Cause
----------
{root_cause['reason']}

Suggested Actions
-----------------
"""

    for action in recommendations["actions"]:
        commentary += f"\n• {action}"

    commentary += f"""

Source
------
{analysis['source_link']}
"""

    return commentary