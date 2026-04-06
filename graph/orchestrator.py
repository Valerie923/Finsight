import os
import sys
from dotenv import load_dotenv
from groq import Groq
load_dotenv(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '.env'))
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import json

from tools.stock_tool import get_stock_info
from tools.news_tool import get_stock_news
from agents.advisor_agent import get_advice


def classify_question(question):
    client = Groq(
        api_key = os.environ.get("GROQ_API")
    )
    chat_completion = client.chat.completions.create(
        messages  = [
            {
                "role": "system", 
                "content": "You are a classifier. Given a question, return ONLY a JSON object with two fields: ticker (eg. TSLA, AAPL, NVDA, AMZN) and route (one of price, news, advice). No other text."
            },
            {
                "role": "user",
                "content": "{question}".format(question=question)
            },
        ],
        model="llama-3.3-70b-versatile",
    )
    return json.loads(chat_completion.choices[0].message.content)

def run_pipeline(question):
    classification = classify_question(question)
    ticker = classification['ticker']
    route = classification['route']
    if route == 'price':
        
        return get_stock_info(ticker)
    elif route == 'news':
       
        return get_stock_news(ticker)
    elif route == 'advice':
        return get_advice(ticker, question)
    else:
        return "Sorry, I couldn't classify your question."

if __name__ == "__main__":
    print(run_pipeline("What's the latest news on Apple?"))
    print(run_pipeline("What is TSLA's current price?"))
    print(run_pipeline("Should I buy more NVDA?"))

