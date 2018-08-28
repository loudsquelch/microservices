from flask import Blueprint, jsonify

version_blueprint = Blueprint("version", __name__)

@version_blueprint.route("/api/version", methods=["GET"])
def get_api_version():
    return jsonify({
        "version": "1.0",
        "status": "success"
    })