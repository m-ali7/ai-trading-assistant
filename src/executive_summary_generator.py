def format_driver_name(driver: str) -> str:
    """
    Converts machine-readable driver names into human-readable labels.

    Example:
    traffic_decline -> Traffic Decline
    conversion_decline -> Conversion Decline
    """

    return driver.replace("_", " ").title()


def generate_executive_summary(category_results: list) -> str:
    """
    Creates a short executive summary across all categories in a manager's brief.
    """

    if not category_results:
        return "No category results available."

    # Sort categories by worst revenue performance first
    sorted_results = sorted(
        category_results,
        key=lambda x: x["analysis"]["revenue_change_pct"]
    )

    worst_category = sorted_results[0]
    worst_analysis = worst_category["analysis"]
    worst_root_cause = worst_category["root_cause"]

    primary_driver = format_driver_name(worst_root_cause["primary_driver"])
    confidence = worst_root_cause["confidence"].title()

    summary = f"""
EXECUTIVE SUMMARY
-----------------
Top Priority: {worst_analysis['market']} {worst_analysis['category']}

Revenue Movement: {worst_analysis['revenue_change_pct']:.2f}% WoW
Primary Driver: {primary_driver}
Confidence: {confidence}

Recommended Focus:
{worst_category['recommendations']['rationale']}
"""

    return summary