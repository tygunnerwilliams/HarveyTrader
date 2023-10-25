import requests
from config_final import Config
from utilities import fetch_google_search_results, extract_stock_price_from_google, extract_news_headlines_from_google

class DataManager:

    @staticmethod
    def get_stock_price(stock_name):
        return extract_stock_price_from_google(stock_name)

    @staticmethod
    def get_stock_news(stock_name):
        return extract_news_headlines_from_google(stock_name)

    @staticmethod
    def get_sentiment_analysis(text):
        if "positive" in text.lower():
            return "Positive"
        elif "negative" in text.lower():
            return "Negative"
        else:
            return "Neutral"