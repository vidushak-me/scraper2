from scraping_file import *
from create_table import *
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/api/scrape', methods=['post'])
def get_scraped_data():
    # this function will scrape data from a website whose url is given
    data = request.get_json()
    url = data.get("url", " ")
    article = get_scraped(url)
    content = insert_in_database(article)
    return jsonify({'data': content})


@app.route('/api/database', methods=['post'])
def get_databse():
    content = get_database_table()
    return jsonify({'data': content})


if __name__ == '__main__':
    app.run(debug=True)
