Project 1
Using Python and Flask, this takes web articles scraped from international English language news organizations into JSON 
files and stores article content using mongoDB.  It displays the contents of the database in a simple web application.

First, run read_data to process the JSON file.  Then, launch the Flask application to display the contents of the database.

If the read_data.py file is not successfuly, the JSON file can be imported using the command line:
mongod --dbpath /usr/local/mongodb-data

Future improvements:
1. Improve Flask design
2. Add NLP functionality
3. improve project organization
