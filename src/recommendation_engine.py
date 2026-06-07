def recommend_actions(root_cause: dict) -> dict:
    """
    Recommend commercial actions based on the identified root cause.

    This is deliberately rule-based for the prototype so that the actions are
    explainable and controlled. In production, this could be expanded using
    approved trading playbooks retrieved through Azure AI Search.
    """

    driver = root_cause["primary_driver"]

    recommendations = {
        "actions": [],
        "rationale": "",
    }

    if driver == "conversion_decline":
        recommendations["actions"] = [
            "Review product detail pages for the affected category.",
            "Check stock availability for top-selling SKUs.",
            "Review pricing and promotion competitiveness.",
            "Investigate checkout or app friction affecting purchase completion.",
        ]
        recommendations["rationale"] = (
            "Traffic is stable or increasing, but fewer visitors are purchasing. "
            "This points to conversion friction rather than demand loss."
        )

    elif driver == "traffic_decline":
        recommendations["actions"] = [
            "Review paid media and CRM campaign performance.",
            "Check SEO visibility and channel traffic trends.",
            "Investigate whether competitor campaigns reduced customer acquisition.",
            "Consider reallocating spend toward higher-performing channels."
        ]
        recommendations["rationale"] = (
            "Revenue moved down alongside traffic, suggesting fewer customers reached the site or app."
        )

    elif driver == "margin_pressure":
        recommendations["actions"] = [
            "Review discount depth and promotional mechanics.",
            "Check whether sales shifted toward lower-margin products.",
            "Compare competitor pricing activity.",
            "Review whether margin pressure is acceptable for strategic volume growth."
        ]
        recommendations["rationale"] = (
            "Gross margin declined materially, suggesting profitability pressure."
        )

    else:
        recommendations["actions"] = [
            "Continue monitoring weekly performance.",
            "Review category-level trends for emerging movement.",
            "Check whether any isolated product-level issues require action."
        ]
        recommendations["rationale"] = (
            "No major negative trading driver was detected."
        )

    return recommendations