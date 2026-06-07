def identify_root_cause(analysis: dict) -> dict:
    """
    Identify the likely root cause behind a category performance movement.

    The input is the output from analysis_engine.py.
    The output is a simple business explanation that can later be used
    by the Monday brief or chat assistant.
    """

    revenue_change = analysis["revenue_change_pct"]
    traffic_change = analysis["traffic_change_pct"]
    conversion_change = analysis["conversion_change_pct"]
    margin_change = analysis["margin_change_pct"]

    # Default result if there is no major issue.
    result = {
        "primary_driver": "stable_performance",
        "reason": "No major negative movement detected.",
        "suggested_action": "Continue monitoring performance.",
        "confidence": "medium",
    }

    # Case 1: Revenue is down, traffic is stable/up, but conversion is down.
    # This usually means people are visiting but not buying.
    if revenue_change < 0 and traffic_change >= 0 and conversion_change < 0:
        result = {
            "primary_driver": "conversion_decline",
            "reason": "Revenue declined despite stable or increasing traffic, indicating that fewer visitors converted into customers.",
            "suggested_action": "Review product pages, pricing, promotions, stock availability, and checkout friction.",
            "confidence": "high",
        }

    # Case 2: Revenue is down and traffic is also down.
    # This usually points to acquisition/marketing/channel performance.
    elif revenue_change < 0 and traffic_change < 0:
        result = {
            "primary_driver": "traffic_decline",
            "reason": "Revenue declined alongside traffic, indicating fewer customers reached the site or app.",
            "suggested_action": "Review marketing channels, campaign performance, SEO visibility, and paid media spend.",
            "confidence": "high",
        }

    # Case 3: Margin is down even if revenue is not the main issue.
    # This usually suggests discounting or profitability pressure.
    elif margin_change < -2:
        result = {
            "primary_driver": "margin_pressure",
            "reason": "Gross margin declined materially, suggesting increased discounting, weaker product mix, or cost pressure.",
            "suggested_action": "Review discount depth, promotional strategy, product mix, and competitor pricing.",
            "confidence": "medium",
        }

    return result