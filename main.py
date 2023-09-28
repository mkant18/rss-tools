# Path: main.py
import yaml
import os
import feedparser

try:
    with open("environment.yml", "r") as f:
        config = yaml.safe_load(f)
except:
    print("Error loading environment.yml")

def fetch_rss_feed(url):
    feed = feedparser.parse(url)
    return feed.entries

def filter_articles(articles, keywords):
    filtered_articles = []
    for article in articles:
        if any(keyword.lower() in article.title.lower() for keyword in keywords):
            filtered_articles.append(article)
    return filtered_articles


def main():
    processed_articles = []
    for i in config['rss_feeds']:
        articles = fetch_rss_feed(i)
        keywords = config['context_keywords']
        filtered_articles = filter_articles(articles, keywords)
        processed_articles.append(filtered_articles)
    return processed_articles