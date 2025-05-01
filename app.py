from flask import Flask, request
from twilio_helper import handle_call

app = Flask(__name__)

@app.route("/voice", methods=["POST"])
def voice():
    return handle_call()

if __name__ == "__main__":
    app.run(port=5000)
