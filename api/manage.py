from flask.cli import FlaskGroup

from project import app
# from flask import Flask, jsonify

# # instantiate app
# app = Flask(__name__)

# @app.route("/ping", methods=["GET"])
# def ping_pong():
#     return jsonify({
#         "status": "success",
#         "message": "pong!"
#     })

cli = FlaskGroup(app)

if __name__ == "__main__":
    cli()