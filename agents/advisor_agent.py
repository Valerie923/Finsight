import os
import sys
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '.env'))
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import requests
from market_agent import get_market_summary

import portfolio

from groq import Groq


def get_advice(ticker, question):
    market_summary = get_market_summary(ticker)
    client = Groq(
        api_key = os.environ.get("GROQ_API")
    )
    chat_completion = client.chat.completions.create(
        messages = [
            {
            "role": "system",
            "content": "You are a financial advisor. The user has this portfolio: {portfolio}, and you are armed with this advice: {market_summary}. Based on this information, provide actionable advice to the user.".format(portfolio=portfolio.get_portfolio(), market_summary=market_summary)
        },
        {
            "role": "user",
            "content": "{question}".format(question=question) },
        ],
        model="llama-3.3-70b-versatile",
    )
    return chat_completion.choices[0].message.content

if __name__ == "__main__":
    print(get_advice("TSLA", "Should I sell my TSLA today?"))