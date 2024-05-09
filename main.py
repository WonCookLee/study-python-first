from flask import Flask, render_template, request
from weworkremotely_scraper import get_jobs

app = Flask("jobScrapper")



@app.route("/")
def home():
    return render_template("home.html", name="cook")

db = {}

@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    if keyword in db :
        jobs = db[keyword]
    else :
        jobs = get_jobs(keyword)
        db[keyword] = jobs
        
    return render_template("search.html", keyword=keyword, jobs=jobs)


app.run("0.0.0.0")
