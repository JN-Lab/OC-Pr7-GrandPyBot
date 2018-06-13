#! /usr/bin/env python3
# coding: utf-8
import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hnsxpy#fler^n!tq#lfg8o^=g2b1oh9m4fv3lnze&3y-fts@7l'
    GOOGLE_API_KEY = 'AIzaSyDVtCr4EtH2H5sVxt1W6Q7gl35lW7amEvo'
