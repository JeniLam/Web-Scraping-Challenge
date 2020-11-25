from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

#Route to render index.html template using data from Mongo
@app.route('/')
def index():
    # find one record of data from the mongo database
    mars_dict = mongo.db.mars_info.find_one()

    # Return template and data
    return render_template('index.html', mars = mars_dict)

@app.route("/scrape")
def scrape():

    mars_database=mongo.db.mars_info
    print(f"my name is yolanda")

    mars_data = scrape_mars.scrape()
    print(mars_data)

    # update mongo database using update and upsert=True
    mars_database.update({},mars_data, upsert=True)
    # https://stackoverflow.com/questions/14343812/redirecting-to-url-in-flask
    return redirect ("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)