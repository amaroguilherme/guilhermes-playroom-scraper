from flask import Flask, jsonify, request
from flask_cors import CORS
from omelete_scraper import OmeleteScraper
from ign_scraper import IGNScraper

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})

@app.route('/news')
def get_news():
  omelete = OmeleteScraper()
  ign = IGNScraper()

  omelete_news = omelete.get_omelete_news()
  ign_news = ign.get_ign_news()

  news = omelete_news + ign_news

  return jsonify({'news': news}), 200

app.run()