import requests
import openai
import random
from config_final import Config
from utils import fetch_google_search_results, extract_stock_price_from_google, extract_news_headlines_from_google, extract_sentiment_from_google
from models import predict_stock_price

class HarveySpecterPersona:
    def __init__(self):
        self.api_key = Config.GOOGLE_API_KEY

    def get_stock_info(self, stock_name):
        try:
            soup = fetch_google_search_results(stock_name + ' stock price')
            stock_price = extract_stock_price_from_google(soup)
            return stock_price
        except Exception as e:
            return f"Error fetching stock info: {e}"

    def get_stock_news(self, stock_name):
        try:
            soup = fetch_google_search_results(stock_name + ' news')
            headlines = extract_news_headlines_from_google(soup)
            return headlines
        except Exception as e:
            return f"Error fetching news: {e}"

    def get_stock_sentiment(self, stock_name):
        try:
            sentiment = extract_sentiment_from_google(stock_name)
            return sentiment
        except Exception as e:
            return f"Error fetching sentiment: {e}"

    def predict_stock_movement(self, stock_name):
        try:
            prediction = predict_stock_price(stock_name)
            return prediction
        except Exception as e:
            return f"Error predicting stock movement: {e}"

    def give_advice(self, stock_name):
        # Fetch data from Google Search
        stock_price = self.get_stock_info(stock_name)
        news_headlines = self.get_stock_news(stock_name)
        sentiment = self.get_stock_sentiment(stock_name)
        prediction = self.predict_stock_movement(stock_name)
        
        # Set the context for Harvey Specter's personality
        harvey_contexts = [
            "You are Harvey Specter, a top lawyer with a sharp wit and confidence.",
            "Imagine you're Harvey Specter, standing tall in your office overlooking Manhattan, and someone asks for your advice on stocks.",
            "You are Harvey Specter, the best closer in New York City. With a glass of scotch in hand, you're about to give a piece of advice on stocks.",
            "Channeling the confidence and charisma of Harvey Specter, what would you say about this stock?"
        ]
        
        harvey_context = random.choice(harvey_contexts)
        
        # Combine the context, data, and the actual question
        full_question = f"{harvey_context} The current stock price of {stock_name} is {stock_price}. Here are some recent news headlines related to it: {news_headlines}. The sentiment analysis indicates: {sentiment}. Predicted stock movement: {prediction}. What's your take on this?"
        
        # Query ChatGPT
        response = openai.Completion.create(engine='gpt-4', prompt=full_question, max_tokens=150)
        
        return response.choices[0].text.strip()