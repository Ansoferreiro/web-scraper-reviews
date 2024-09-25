# backend/app.py
from flask import Flask, jsonify
from scraper import scrape_reviews

app = Flask(__name__)

@app.route('/reviews', methods=['GET'])
def get_reviews():
    reviews = scrape_reviews()
    return jsonify(reviews)

if __name__ == '__main__':
    app.run(debug=True)
