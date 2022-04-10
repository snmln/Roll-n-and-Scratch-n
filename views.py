from flask import (Blueprint, jsonify, redirect, render_template, request,
                   url_for)

views = Blueprint(__name__, "views")


@views.route("/")
def home():
    return render_template("index.html", name="tim")


@views.route("/profile/")
def profile():
    args = request.args
    name = args.get('name')
    return render_template("profile.html", name=name)


@views.route("/json/")
def get_json():
    return jsonify({'name': 'tim', 'coolness': 10})


@views.route("/data")
def get_data():
    data = request.json
    return jsonify(data)


@views.route("/go-to-home")
def goToHome():
    return redirect(url_for("views.home"))
