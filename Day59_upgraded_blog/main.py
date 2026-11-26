from flask import Flask, render_template
import requests

posts = requests.get("https://api.npoint.io/674f5423f73deab1e9a7").json()
for post in posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_obj)


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
    
@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")           

if __name__ == "__main__":
    #Run the app in debug mode to auto-reload
    app.run(debug=True)
