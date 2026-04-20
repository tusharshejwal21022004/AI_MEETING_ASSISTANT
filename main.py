from flask import Flask, render_template, request
import threading

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/join", methods=["POST"])
def join():
    try:
        from main_local import run_meeting_bot
        link = request.form["meeting_link"]

        bot_thread = threading.Thread(
            target=run_meeting_bot,
            args=(link,),
            daemon=True
        )
        bot_thread.start()

        return f"Meeting bot started for: {link}"

    except Exception as e:
        return f"Join Error: {str(e)}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)