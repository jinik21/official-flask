from flask import Flask, render_template,request, url_for


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/blockchain')
def blockchain():
    return render_template('blockchain.html')

@app.route('/webdev')
def webdev():
    return render_template('webdev.html')


@app.route('/appdev')
def appdev():
    return render_template('appdev.html')

@app.route('/aiml')
def aiml():
    return render_template('aiml.html')


@app.route('/iot')
def iot():
    return render_template('iot.html')


@app.route('/apis')
def apis():
    return render_template('APIs.html')