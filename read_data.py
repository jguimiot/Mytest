import pymongo
import json

# Connect to Mongo db
conn_str = 'mongodb://localhost:21017'
client = pymongo.MongoClient(conn_str)
db = client.news

DATABASE_NAME = 'news-database'
COLLECTION_NAME = 'article-collection'

# Connect to relevant database
db = client[DATABASE_NAME]
# Access specific collection
collection = db[COLLECTION_NAME]

with open('bbc-news.json') as f:
    articles = json.load(f)

article_id = collection.insert_one(articles).inserted_id
client.close()
