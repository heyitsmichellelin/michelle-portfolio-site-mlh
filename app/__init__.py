import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)



@app.route('/')
def index():
    education_data =[
        {"school": "Western University",
         "year": "2021-2025",
         "img": "./static/img/western.jpg"
        },
        {"school": "Ivey Business School",
         "year": "2023-2025",
         "img": "./static/img/ivey.png"}
    ]

    experience_data = [
        {"company":"",
         "logo":"",
         "year":"",
         "description":""}
    ]
    return render_template('index.html',title="MLH Fellow", titleEdu="Education", education_data=education_data, url=os.getenv("URL"))


@app.route('/hobbies')
def get_hobbies_page():
    hobby_data = [
        {"name":"",
         "description":"",
         "image":""}
    ]
    return render_template('hobbies.html', title="Hobbies", url=os.getenv("URL"))

@app.route('/travels')
def get_travels_page():
    return render_template('travels.html', title="Travels", url=os.getenv("URL"))
