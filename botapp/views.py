#! /usr/bin/env python3
# coding: utf-8
"""
This module manages the views
There is only one page for this app
"""

from flask import render_template, url_for, jsonify
from .app import app
from .forms import MessageForm

@app.route('/')
@app.route('/index/')
def index():
    """Initiate the index page"""
    form = MessageForm()
    return render_template('index.html', form=form)

@app.route('/treatment', methods=['POST'])
def message_back():
    return jsonify({'sentence': 'test ajax routine'})
