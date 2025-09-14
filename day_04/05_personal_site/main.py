from flask import Flask, render_template, request, redirect
from datetime import datetime

app = Flask(__name__)
session = {"todos": []}

@app.route("/")
def index():
    now = datetime.now()
    return render_template("landing.html", hour=now.hour)

@app.route("/login/")
def login():
    return "<a href='/login'><h1>Login</h1></a>"

@app.route("/hobby/")
@app.route("/hobbies/")
def hobby():
    hobbies = ['Code','Drunk','Play DOTA']
    return render_template("hobbies.html", hobbies=hobbies)

@app.route("/opinion/<topic>")
@app.route("/opinions/<topic>")
def topic_dynamic(topic):
    return f"topic {topic}"

@app.route("/foods/")
def food():
    foods = ['Sisig','Lechon','Adobo','Sinigang','Chopsuey']
    return render_template("food.html", foods=foods)

@app.route("/skills/")
def skills():
    skill_levels = {
        "Painting": "Intermediate",
        "Dancing": "Abysmal",
        "Singing": "Poor",
        "Translation": "Proficient",
        "Eating": "Professional"
    }
    return render_template("skills.html", skills=skill_levels)

@app.get("/todo/")
def show_todo():
    return render_template("todo.html", todos=session["todos"])

@app.post("/todo/")
def add_todo():
    if request.form["todo"]:
        session["todos"].append(request.form["todo"])
    return redirect("/todo/")

app.run()
