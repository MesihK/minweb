import flask
from flask import render_template, session, redirect, url_for, request, flash, send_file
from flask_bootstrap import Bootstrap5
import jinja2

import eventlet
eventlet.monkey_patch()

app = flask.Flask(__name__)
bootstrap = Bootstrap5(app)
app.config['SECRET_KEY'] = 'secret!'

@app.route('/', methods=['GET'])
def index():
    with open('static/AVX54569.1/AVX54569.1.B3R0R7.100.html','r') as f:
        return render_template('index.jinja2', title='',aln=f.read())

@app.route('/disclaimer', methods=['GET'])
def disclaimer():
    return render_template('disclaimer.jinja2', title='Disclaimer')
