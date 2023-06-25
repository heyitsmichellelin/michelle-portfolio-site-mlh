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
    return render_template('index.html',title="MLH Fellow", titleEdu="Education", education_data=education_data, url=os.getenv("URL"))
