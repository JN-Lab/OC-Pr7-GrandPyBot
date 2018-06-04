#! /usr/bin/env python3
# coding: utf-8
"""
This module manages the views
There is only one page for this app
"""

from flask import render_template, url_for, jsonify, request
from .app import app
from .forms import MessageForm
from .utils.response import Response

@app.route('/')
@app.route('/index/')
def index():
    """Initiate the index page"""
    form = MessageForm()
    return render_template('index.html', form=form)

@app.route('/treatment', methods=['POST'])
def message_back():
    message_entrant = {}
    if request.is_json:
        message_entrant = request.get_json()
    treatment = Response()
    return jsonify(treatment.get_info(message_entrant))
