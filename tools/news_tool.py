import os
import requests
from dotenv import load_dotenv

load_dotenv()

newsapi = os.getenv("NEWS_API")
def get_stock_news(company_name):
    url = f"https://newsapi.org/v2/everything"
    params = {
        "q": company_name,
        "apiKey": newsapi,
        "pageSize": 3,
        "sortBy": "publishedAt",
        "language": "en"
    }
    response = requests.get(url, params=params)
    data = response.json()
    articles = data.get("articles", [])
    return [{"title": article["title"], "url": article["url"]} for article in articles[:3]]

if __name__ == "__main__":
    print(get_stock_news("Tesla"))