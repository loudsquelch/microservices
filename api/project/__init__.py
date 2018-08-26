import os
import sys
from flask import Flask, jsonify

# instantiate app
app = Flask(__name__)

# set config
app_settings = os.getenv("APP_SETTINGS")
app.config.from_object(app_settings)

#print(app.config, file=sys.stderr)

@app.route("/api/version", methods=["GET"])
def ping_pong():
    return jsonify({
        "version": "1.0"
    })