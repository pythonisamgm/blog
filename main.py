from flask import Flask, render_template, request
import json
from datetime import datetime
import os, random
import smtplib

app = Flask (__name__)
poster = "Mirti"
miguel_bod = datetime(2023, 3, 19)
year = datetime.now().year

with open("babyplus_data_export.json", "r", encoding='utf-8') as data:
    content = data.read()


#----------------------------------------------------------loading and using json from baby plus app-----------------------------------------
new_dict = json.loads(content)
diario = (new_dict["diarynote"])
file_path = "static/assets/img/dev"

#--------------------------------------------------------extracting Miguel's number of days, post's photo----------------------------------
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




@app.route('/')
def home():
    return render_template("index2.html", diario=diario, poster=poster, year=year)

@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/')
def index():
    return render_template("index2.html")

@app.route('/post/<post_id>')
def post(post_id):
    id_int = int(post_id)
    print(id_int)
    post = diario[len(diario) - id_int -1]
    return render_template("post.html", diario=diario, poster=poster, post=post )



@app.route('/contact', methods=['GET','POST'])
def contact():
    if request.method == "POST":
        data = request.form
        name = data["name"]
        email = data["email"]
        phone = data["phone"]
        message = data["message"]
        send_mail(name, email, phone, message)
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)



#----------------------------------------------------------------------- send email with smtb--------------------------------------------------
my_email = os.getenv("EMAIL")
my_password = os.getenv("PASSWORD")

def send_mail(name, email, phone, message):
    file_content =f" Name: {name}\n Email: {email}\n Phone: {phone}\n Message: {message}"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        #securing the email server. encrypt the mail.
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=my_email,
                            msg= f"Subject:New contact\n\n{file_content}")






if __name__ == "__main__":
    app.run(debug=True)