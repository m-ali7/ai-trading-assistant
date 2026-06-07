import pandas as pd


def calculate_weekly_change(current, previous):
    """
    Calculate percentage change between two values.
    """

    if previous == 0:
        return 0

    return round(((current - previous) / previous) * 100, 2)


def analyse_category(df, market, category):
    """
    Compare latest week vs previous week for a market/category.
    """

    filtered = df[
        (df["market"] == market)
        & (df["category"] == category)
    ]

    filtered = filtered.sort_values("week_start", ascending=False)

    current_week = filtered.iloc[0]
    previous_week = filtered.iloc[1]

    results = {
        "market": market,
        "category": category,
        "revenue_change_pct": calculate_weekly_change(
            current_week["revenue"],
            previous_week["revenue"]
        ),
        "traffic_change_pct": calculate_weekly_change(
            current_week["traffic"],
            previous_week["traffic"]
        ),
        "conversion_change_pct": calculate_weekly_change(
            current_week["conversion_rate"],
            previous_week["conversion_rate"]
        ),
        "margin_change_pct": calculate_weekly_change(
            current_week["gross_margin"],
            previous_week["gross_margin"]
        ),
        "source_link": current_week["source_link"]
    }

    return results