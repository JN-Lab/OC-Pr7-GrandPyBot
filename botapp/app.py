#! /usr/bin/env python3
# coding: utf-8
"""This module manages the app creation"""

from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
