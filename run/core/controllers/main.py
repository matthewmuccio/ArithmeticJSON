#!/usr/bin/env python3


from flask import Blueprint, jsonify, redirect, render_template, request, session, url_for


controller = Blueprint("main", __name__, url_prefix="/")

@controller.route("", methods=["GET"])
def show_main():
    return render_template("main.html")

@controller.route("/add", methods=["GET"])
def add():
    num1 = request.args.get("num1", default=0.0, type=float)
    num2 = request.args.get("num2", default=0.0, type=float)
    expression = "{0} + {1}".format(num1, num2)
    result = "{0}".format(num1 + num2)
    return jsonify(expression=expression, result=result)

@controller.route("/subtract", methods=["GET"])
def subtract():
    num1 = request.args.get("num1", default=0.0, type=float)
    num2 = request.args.get("num2", default=0.0, type=float)
    expression = "{0} - {1}".format(num1, num2)
    result = "{0}".format(num1 - num2)
    return jsonify(expression=expression, result=result)

@controller.route("/multiply", methods=["GET"])
def multiply():
    num1 = request.args.get("num1", default=0.0, type=float)
    num2 = request.args.get("num2", default=0.0, type=float)
    expression = "{0} * {1}".format(num1, num2)
    result = "{0}".format(num1 * num2)
    return jsonify(expression=expression, result=result)

@controller.route("/divide", methods=["GET"])
def divide():
    num1 = request.args.get("num1", default=0.0, type=float)
    num2 = request.args.get("num2", default=0.0, type=float)
    expression = "{0} / {1}".format(num1, num2)
    result = "{0}".format(num1 / num2)
    return jsonify(expression=expression, result=result)