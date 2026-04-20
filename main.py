from flask import Flask, render_template, request
from meeting_connector.connect_meeting import open_meeting

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/join", methods=["POST"])
def join():
    link = request.form["meeting_link"]
    open_meeting(link)
    return f"Joining meeting: {link}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)