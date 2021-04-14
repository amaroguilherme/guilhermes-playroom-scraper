import random
from flask import Flask, jsonify, request
from flask_cors import CORS
from omelete_scraper import OmeleteScraper
from gamespot_scraper import GamespotScraper
from cache import cache

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})
cache.init_app(app)

@app.route('/news')
@cache.cached(timeout=21600, key_prefix='news')
def get_news():

  omelete = OmeleteScraper()
  gamespot = GamespotScraper()

  omelete_news = omelete.get_omelete_news()
  gamespot_news = gamespot.get_gamespot_news()

  news = omelete_news + gamespot_news
  random.shuffle(news)

  return jsonify({'news': news}), 200

app.run()