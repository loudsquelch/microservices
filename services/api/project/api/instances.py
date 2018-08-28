from flask import Blueprint, jsonify
from project.api.models import Instance

instances_blueprint = Blueprint("instances", __name__)

@instances_blueprint.route("/instances", methods=["GET"])
def get_all_instances():
    """Get all instances"""
    response_object = {
        "status": "fail",
        "message": "not implemented"
    }
    return jsonify(response_object), 404

@instances_blueprint.route("/instances/", methods=["GET"])
def get_single_instance_no_id():
    """Get all instances"""
    response_object = {
        "status": "fail",
        "message": "please specify instance id"
    }
    return jsonify(response_object), 404

@instances_blueprint.route("/instances/<instance_id>", methods=["GET"])
def get_single_instance(instance_id):
    """Get single instance details"""
    response_object = {
        "status": "fail",
        "message": "instance does not exist"
    }
    try:
        instance = Instance(instance_id)
        if not instance:
            return jsonify(response_object), 404
        else:
            response_object = {
                "status": "success",
                "data": {
                    "instance_id": instance.id,
                    "scope": instance.scope
                }
            }
            return jsonify(response_object), 200
    except KeyError:
        return jsonify(response_object), 404