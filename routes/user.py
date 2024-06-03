from flask import Blueprint, jsonify

import db.users as users_db

user = Blueprint("user", __name__)


@user.route("/user", methods=["GET"])
def get_user():
    user = users_db.get_user_by_id("fb79067b-2f7a-44a5-836a-cc503e5335d4")
    user_dict = user.to_dict()
    return jsonify(user_dict)


@user.route("/user", methods=["POST"])
def create_user():

    email = "wedc@ccsd.com"
    raw_user_meta_data = {"name": "Wedc"}
    user = users_db.create_user(email, raw_user_meta_data)
    user_dict = user.to_dict()
    return jsonify(user_dict)


@user.route("/user", methods=["PUT"])
def update_user():
    return jsonify({"message": "PUT user"})
