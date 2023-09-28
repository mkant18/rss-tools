# Path: main.py
import yaml
import os
import feedparser

try:
    with open("environment.yml", "r") as f:
        config = yaml.safe_load(f)
except:
    print("Error loading environment.yml")



def config_to_feed():
    filename = config['rss_feeds']
    print(filename)
    with open(filename, "r") as f:
        rss_feeds = f.read().split(",")
    return rss_feeds

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
    for i in config_to_feed():
        articles = fetch_rss_feed(i)
        keywords = config['context_keys']
        filtered_articles = filter_articles(articles, keywords)
        processed_articles.append(filtered_articles)
    return processed_articles

if __name__ == "__main__":
    outputs = main()
    print(type(outputs))
    print(type(outputs[0]))
    print(type(outputs[0][0]))
    print(outputs[0][0].keys())
    print(outputs[0][0].summary)
