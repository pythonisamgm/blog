from flask import Flask, render_template
import json
from datetime import datetime
import os, random

app = Flask (__name__)
poster = "Mirti"
miguel_bod = datetime(2023, 3, 19)

with open("babyplus_data_export.json", "r", encoding='utf-8') as data:
    content = data.read()



new_dict = json.loads(content)
diario = (new_dict["diarynote"])
file_path = "static/assets/img/dev"

num = len(diario)

for n in diario:

    post_date = n["date"].split("T")[0]
    formated_date = datetime.strptime(post_date, "%Y-%m-%d")
    complete_datetime = formated_date - miguel_bod
    days_of_life = complete_datetime.days
    n["day"] = days_of_life
    num -= 1
    n["id"] = num
    if n["photo"] == "":
        n["photo"] = "dev/" + random.choice(os.listdir(file_path))


year = datetime.now().year

@app.route('/')
def home():
    return render_template("index2.html", diario=diario, poster=poster, year=year)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/')
def index():
    return render_template("index2.html")

@app.route('/post/<post_id>')
def post(post_id):
    id_int = int(post_id)
    print(id_int)
    post = diario[len(diario) - id_int -1]
    return render_template("post.html", diario=diario, poster=poster, post=post )



if __name__ == "__main__":
    app.run(debug=True)