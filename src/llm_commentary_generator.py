import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_llm_commentary(analysis: dict, root_cause: dict, recommendations: dict) -> str:
    """
    Uses GPT to turn grounded trading facts into executive-friendly commentary.

    Important:
    Python calculates the numbers.
    GPT only explains the already-calculated facts.
    """

    model = os.getenv("OPENAI_MODEL", "gpt-4.1")

    prompt = f"""
You are an AI trading assistant for a large European fashion e-commerce retailer.

Write a concise weekly trading brief for a trading manager.

Use ONLY the facts below. Do not invent any numbers, causes, or sources.

Facts:
Market: {analysis["market"]}
Category: {analysis["category"]}
Revenue change WoW: {analysis["revenue_change_pct"]:.2f}%
Traffic change WoW: {analysis["traffic_change_pct"]:.2f}%
Conversion change WoW: {analysis["conversion_change_pct"]:.2f}%
Margin change WoW: {analysis["margin_change_pct"]:.2f}%

Root cause:
{root_cause["reason"]}

Recommended actions:
{recommendations["actions"]}

Source:
{analysis["source_link"]}

Format your response with these sections:
1. Headline
2. Commentary
3. Suggested Actions
4. Source
"""

    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": (
                    "You write concise, commercially useful trading briefs. "
                    "You never invent numbers. You only use the provided facts."
                ),
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
        temperature=0.2,
    )

    return response.choices[0].message.content