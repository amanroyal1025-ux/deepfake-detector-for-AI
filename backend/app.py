from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route("/check")
def check():
    return jsonify({"result": random.choice(["Real Video", "Fake / Scam"])})
