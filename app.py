from flask import Flask, jsonify, request
from flask_cors import CORS
from omelete_scraper import OmeleteScraper

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})

@app.route('/news')
def get_news():
  omelete = OmeleteScraper()

  omelete_news = omelete.get_omelete_news()

  news = omelete_news

  return jsonify({'news': news}), 200

app.run()