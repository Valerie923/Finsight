import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from tools.stock_tool import get_stock_info
from tools.news_tool import get_stock_news


def get_market_summary(ticker):
    market_info = get_stock_info(ticker)
    summary = "{company} is currently priced at {price} USD with a change of {change_percent}%.".format(**market_info)
    news = get_stock_news(ticker)
    for i, article in enumerate(news):
        summary += f"\nNews {i+1}: {article['title']} - {article['url']}"
    return summary

if __name__ == "__main__":
    print(get_market_summary("TSLA"))
