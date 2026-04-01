import yfinance as yf

def get_stock_info(ticker):
    stock = yf.Ticker(ticker)
    info = stock.info
    
    return {
        "company": info.get("longName"), 
        "price": info.get("currentPrice"), 
        "change_percent": info.get("regularMarketChangePercent")
    }
if __name__ == "__main__":
    print(get_stock_info("TSLA"))
    