from bs4 import BeautifulSoup
import requests

class OmeleteScraper:

  def get_article_content(self, article_url):
    article_paragraphs = list()
    html_content = requests.get(article_url).content
    soup_content = BeautifulSoup(html_content, 'html.parser')

    content = soup_content.find("div", {"class": "article__body article--content"})
    content_sequence = content.findAll("p")

    for paragraph in content_sequence:
      article_paragraphs.append(paragraph.get_text())

    return article_paragraphs

  def get_omelete_news(self):
    target = "https://www.omelete.com.br"
    news = list()

    html = requests.get("https://www.omelete.com.br/").content
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.findAll("a", class_="analytic-featured")

    for element in links:
      results = element.find("img", {"data-lazy-src" : True})
      if results is not None:
        article = dict()
        article["image"] = f'https:{results.get("data-lazy-src")}'
        article["title"] = element.find("h2").string
        article["content"] = self.get_article_content(f'{target}{element.get("href")}')
        news.append(article)

    return news


