import os
import requests
from flask import Flask, render_template
from dotenv import load_dotenv

# Load API Key from .env
load_dotenv()
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

app = Flask(__name__)

def fetch_news():
    url = f"https://newsapi.org/v2/everything?q=technology&language=en&pageSize=50&sortBy=publishedAt&apiKey={NEWS_API_KEY}"
    response = requests.get(url)
    return response.json().get("articles", [])

def load_interests():
    with open("interests.txt", "r") as file:
        return [line.strip().lower() for line in file.readlines()]

def filter_articles(articles, interests):
    filtered = []
    for article in articles:
        text = (article.get("title", "") + " " + article.get("description", "")).lower()
        if any(interest in text for interest in interests):
            filtered.append(article)
    return filtered[:15]

@app.route("/")
def index():
    articles = fetch_news()
    interests = load_interests()
    relevant_articles = filter_articles(articles, interests)
    return render_template("index.html", articles=relevant_articles)

if __name__ == "__main__":
    app.run(debug=True)
