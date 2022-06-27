import flask
from flask import render_template, session, redirect, url_for, request, flash, send_file
from flask_bootstrap import Bootstrap5
import jinja2
from pickle import load

import eventlet
eventlet.monkey_patch()

app = flask.Flask(__name__)
bootstrap = Bootstrap5(app)
app.config['SECRET_KEY'] = 'secret!'


with open('jcvi.prost.db.pkl','rb') as f:
    db = load(f)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.jinja2', title='Home')

@app.route('/disclaimer', methods=['GET'])
def disclaimer():
    return render_template('disclaimer.jinja2', title='Disclaimer')

@app.route('/result', methods=['GET'])
def result():
    pid = request.args.get('p', default = '', type = str)
    if pid == '' or pid not in db:
        return render_template('index.jinja2',title='%s not found'%pid)
    res = db[pid]
    return render_template('result.jinja2',title='Results',pid=pid,res=res)
    
