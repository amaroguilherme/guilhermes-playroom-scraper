from bs4 import BeautifulSoup
import requests

class GamespotScraper:

  def get_article_content(self, article_url):
    article_paragraphs = list()
    html_content = requests.get(article_url).content
    soup_content = BeautifulSoup(html_content, 'html.parser')

    content = soup_content.find("div", {"class": "content-entity-body"})
    content_paragraphs = content.findAll("p")

    for paragraph in content_paragraphs:
      article_paragraphs.append(paragraph.get_text())

    return article_paragraphs

  def get_gamespot_news(self):
    news = list()
    html = requests.get("https://www.gamespot.com/news/").content
    soup = BeautifulSoup(html, 'html.parser')

    links = soup.findAll("div", {"class": "card-item"})

    for section in links:
      article = dict()
      article["image"] = section.find("div", {"class": "card-item__img"}).find("img").get("src")
      article["title"] = section.find("div", {"class": "card-item__content"}).find("h4").string
      article["content"] = self.get_article_content(f'https://www.gamespot.com{section.find("div", {"class": "card-item__content"}).find("a").get("href")}')
      news.append(article)

    return news

