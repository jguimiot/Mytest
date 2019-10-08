## Project 1
Using Python and Flask, this takes web articles scraped from international English language news organizations into JSON 
files and stores article content using mongoDB.  It displays the contents of the database in a simple web application.

Start the mongod instance with the following command:
 - mongod --dbpath /usr/local/mongodb-data

Then, load the sample data into the mongo dabase by running "read_data.py".

As an alternative to using the read_data.py program you can also use the "mongoimport" command from a terminal as follows:
 - mongoimport --db newsdatabase --collection articlecollection --file bbc.json --jsonArray

Then, launch the Flask application to display the contents of the database.

#### Future improvements:
1. Improve Flask design
2. Add NLP functionality
3. improve project organization
