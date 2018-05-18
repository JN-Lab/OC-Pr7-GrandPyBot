#! /usr/bin/env python3
# coding: utf-8
from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired

class MessageForm(FlaskForm):
    message = TextAreaField('Message', validators=[DataRequired])
    submit = SubmitField('Envoi')
