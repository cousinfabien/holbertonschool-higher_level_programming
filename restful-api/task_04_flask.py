#!/usr/bin/python3
"""Task 04 - Basic Flask API"""


from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}


@app.route("/", methods=["GET"])
def home():
    """Root endpoint"""
    return "Welcome to the Flask API!"


@app.route("/data", methods=["GET"])
def get_data():
    """Return list of usernames"""
    return jsonify(list(users.keys()))


@app.route("/status", methods=["GET"])
def status():
    """API status"""
    return "OK"


@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    """Return user data by username"""
    if username not in users:
        return jsonify({"error": "User not found"}), 404
    return jsonify(users[username])


@app.route("/add_user", methods=["POST"])
def add_user():
    """Add a new user"""
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400

    data = request.get_json()
    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409
    users[username] = data

    return jsonify({"message": "User added", "user": data}), 201


if __name__ == "__main__":
    app.run()
