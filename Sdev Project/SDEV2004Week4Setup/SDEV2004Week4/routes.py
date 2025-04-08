from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return (render_template("index.html"))

@app.route('/about')
def about():
    return (render_template ("about.html"))

@app.route('/products')
def products():
        return (render_template ("products.html"))

@app.route('/store')
def store():
        return (render_template ("store.html"))