import flask
from flask import Flask


app = Flask(__name__)


def get_latest_articles():
    return [
        # link, title, text, company, published
        {'link': 'http://rss.cnn.com/~r/rss/cnn_us/~3/wChjXBLitKg/index.html',
         'title': 'Michigan school resource officer sentenced to 1 year in jail for sexually assaulting 3 high school students',
         'text': 'A former Michigan high school resource officer was sentenced to one year in jail',
         'company': 'cnnUS',
         'published': '2019-10-04T01:01:39'}
    ]


# view method to display news articles
@app.route('/')
def index():
    test_articles = get_latest_articles()
    return flask.render_template('home/index.html', articles=test_articles)

# view method to display the news source
@app.route('/sources')
def sources():
    return flask.render_template('home/sources.html')


if __name__ == '__main__':
    app.run(debug=True)
