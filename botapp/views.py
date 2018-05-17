#! /usr/bin/env python3
# coding: utf-8
from .app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return "Ca fonctionne pour le moment"
