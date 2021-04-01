from bs4 import BeautifulSoup
import requests

class IGNScraper:

  def get_article_content(self, article_url):
    article_paragraphs = list()
    html_content = requests.get(article_url).content
    soup_content = BeautifulSoup(html_content, 'html.parser')

    content = soup_content.find("article")
    content_sequence = content.findAll("p")

    for paragraph in content_sequence:
      article_paragraphs.append(paragraph.get_text())

    return article_paragraphs

  def get_ign_news(self):
    target = "https://br.ign.com"
    news = list()

    html = requests.get("https://br.ign.com/").content
    soup = BeautifulSoup(html, 'html.parser')

    links = soup.findAll("article")

    for link in links:
      if '[Vídeo]' not in link.find("h3").string:
        results = link.find("img")
        article = dict()
        article["image"] = results.get("src")
        article["title"] = link.find("h3").string

        if ' '.join(link.get("class")) != "gallery STORY" and "card VIDEO" not in ' '.join(link.get("class")):
          if target not in link.find("a").get("href"):
            article["content"] = get_article_content(f'{target}{link.find("a").get("href")}')
          else:
            article["content"] = get_article_content(link.find("a").get("href"))
        news.append(article)

    return news

