from flask import Flask, render_template,redirect
from flask_pymongo import PyMongo
import scrape_mars

import sys

app = Flask(__name__)

# setup mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/Mission_to_Mars_DB"
mongo = PyMongo(app)



@app.route("/")
def index():
    print("I am on index.html")
    # write a statement that finds all the items in the db and sets it to a variable
    mars_data=mongo.db.mars_db.find_one()
    # render an index.html template and pass it the data you retrieved from the database
    return render_template("index.html", data=mars_data)

@app.route("/scrape")
def scrape():     
    print("I am in scrape")
    mars_info=scrape_mars.mars_news_scrape()
    mars_info=scrape_mars.img_scrape()
    mars_info=scrape_mars.mars_weather()
    mars_info=scrape_mars.mars_facts()
    mars_info=scrape_mars.mars_hem()
    mongo.db.mars_db.update({},mars_info,upsert=True)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
