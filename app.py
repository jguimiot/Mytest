from flask import Flask

# from data import mongo_setup
# from data.users import User

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


# view method to display html templates
@app.route('/')
def index():
    test_articles = get_latest_articles()
    return flask.render_template('home/index.html', articles=test_articles)


@app.route('/sources')
def sources():
    return flask.render_template('home/sources.html')


# def setup_db():
#    mongo_setup.global_init()
#
#    user = User()
#    user.name = 'Julia Guimiot'
#    user.email = 'test@email.com'


if __name__ == '__main__':
    app.run(debug=True)
