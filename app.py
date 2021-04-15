import random
from flask import Flask, jsonify, request
from flask_cors import CORS
from omelete_scraper import OmeleteScraper
from gamespot_scraper import GamespotScraper
from cache import cache

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})
cache.init_app(app)

@app.route('/omelete')
@cache.cached(timeout=21600, key_prefix='omelete')
def get_omelete():

  omelete = OmeleteScraper()

  omelete_news = omelete.get_omelete_news()

  return jsonify({'news': omelete_news}), 200

@app.route('/gamespot')
@cache.cached(timeout=21600, key_prefix='gamespot')
def get_gamespot():

  gamespot = GamespotScraper()

  gamespot_news = gamespot.get_gamespot_news()

  return jsonify({'news': gamespot_news}), 200

app.run()