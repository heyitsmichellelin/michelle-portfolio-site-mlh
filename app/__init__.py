import os
from flask import Flask, render_template, request, json

from peewee import *
from playhouse.shortcuts import model_to_dict
import datetime

from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

mydb = MySQLDatabase( os.getenv("MYSQL_DATABASE"),
                        host=os.getenv("MYSQL_HOST"),
                        port=3306,
                        user=os.getenv("MYSQL_USER"),
                        passwd=os.getenv("MYSQL_PASSWORD"))

class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = CharField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = mydb

mydb.connect()
mydb.create_tables([TimelinePost])

@app.route('/')
def index():
    education_data =[
        {"school": "Western University",
         "year": "2021-2025",
         "img": "./static/img/western.jpg"
        },
        {"school": "Ivey Business School",
         "year": "2023-2025",
         "img": "./static/img/ivey.png"
         },
        {"school": "University of California, Irvine",
         "year": "2021-24",
          "img": "./static/img/uci_logo.png"
        }
    ]

    experience_data = [
        {"company":"Vibemap",
            "title" : "Development Intern",
            "logo":"./static/img/experienceImages/vibemap.jpeg",            
            "date":"May 14, 2023 - Present",
            "description":"Worked as a development intern for the vibemap startup. Learned skills in React, React Native, and Wordpress."},
        
        {"company":"MLH Fellowship",
            "title" : "Site Reliability Engineering Fellow",
            "logo":"./static/img/experienceImages/mlh.png",
            "date": "June 04, 2021 - Present",
            "description":"Worked as a fellow for the MLH Fellowship. Learned skills in React, Flask, and Python."},
        
        {"company":"Western University",
            "title" : "Programming Peer tutor",
            "logo":"./static/img/western.jpg",
            "date":"September 2021 - Present",
            "description":"Worked as a programming peer tutor at Western University. Learned skills in Java, Python, and C++."},

    ]
    return render_template('index.html',title="MLH Fellow", titleEdu="Education", education_data=education_data, titleExp="Experience" ,  experience=experience_data, url=os.getenv("URL"))


@app.route('/hobbies')
def get_hobbies_page():
    # load json data with hobbies, then pass it to the template
    filename = os.path.join(app.static_folder, 'data', 'data.json')
    data = json.load(open(filename))    

    return render_template('hobbies.html', title="Hobbies", url=os.getenv("URL"), data=data['hobbies'])


@app.route('/travels')
def get_travels_page():
    return render_template('travels.html', title="Travels", url=os.getenv("URL"))


@app.route('/api/timeline_post', methods=['POST'])
def create_timeline_post():
    name = request.form.get('name')
    email = request.form.get('email')
    content = request.form.get('content')
    timeline_post = TimelinePost.create(name=name, email=email, content=content)

    return model_to_dict(timeline_post)

@app.route('/api/timeline_post', methods=['GET'])
def get_timeline_posts():
    return {
        'timeline_posts': [
            model_to_dict(p)
            for p in 
            TimelinePost.select().order_by(TimelinePost.created_at.desc())
        ]
    }

@app.route('/api/timeline_post/<int:timeline_post_id>', methods=['DELETE'])
def delete_timeline_post(timeline_post_id):
    TimelinePost.delete_by_id(timeline_post_id)
    return {}