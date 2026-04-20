from flask import Flask, render_template, request
from main_local import run_meeting_bot
import threading

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/join", methods=["POST"])
def join():
    link = request.form["meeting_link"]

    try:
        bot_thread = threading.Thread(target=run_meeting_bot, args=(link,))
        bot_thread.start()
        return f"Meeting bot started for: {link}"

    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)