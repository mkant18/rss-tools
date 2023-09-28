# Path: main.py
import yaml
import os
import feedparser

try:
    with open("environment.yml", "r") as f:
        config = yaml.safe_load(f)
except:
    print("Error loading environment.yml")

class Article:
    def __init__(self, title, summary, link):
        self.title = title
        self.summary = summary
        self.link = link

    def __str__(self):
        return f"{self.title}\n{self.summary}\n{self.link}\n"

    def __repr__(self):
        return f"{self.title}\n{self.summary}\n{self.link}\n"


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
    final_articles = []
    for article in processed_articles:
        if article == [] or article == None:
            pass
        else:
            print(article)
            current = Article(article.title, article.summary, article.link)
            final_articles.append(current)
    return final_articles

if __name__ == "__main__":
    print(main())