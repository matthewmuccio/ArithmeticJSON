#!/usr/bin/env python3


from flask import Blueprint, jsonify, redirect, render_template, request, session, url_for


controller = Blueprint("main", __name__, url_prefix="/")

@controller.route("/add", methods=["GET"])
def add():
    return render_template("main.html")

@controller.route("/subtract", methods=["GET"])
def subtract():
    return render_template("main.html")

@controller.route("/multiply", methods=["GET"])
def multiply():
    return render_template("main.html")

@controller.route("/divide", methods=["GET"])
def divide():
    return render_template("main.html")