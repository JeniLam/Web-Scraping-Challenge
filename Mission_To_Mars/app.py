from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app

#Route to render index.html template using data from Mongo
@app.route("/")
def scrape():

    # find one record of data from the mongo database
    mars_dict = mongo.db_mars_dict.find_one()

    # Return template and data
    return render_template('index.html', mars = mars_dict)