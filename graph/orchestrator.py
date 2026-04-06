import os
import sys
from dotenv import load_dotenv
from groq import Groq
load_dotenv(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '.env'))
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import json


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
if __name__ == "__main__":
    print(classify_question("Should I sell my Tesla stock?"))
