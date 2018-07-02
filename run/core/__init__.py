#!/usr/bin/env python3


import os

from flask import Flask

from core.controllers.main import controller as main


omnibus = Flask(__name__)

omnibus.secret_key = b"pickle_fish_lips"

omnibus.register_blueprint(main)