from flask import Flask, render_template,request, url_for


app = Flask(__name__)
ads="admin"
passwordc="hello"
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/home')
def homee():
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

@app.route('/login',methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        admin=request.form.get("admin")
        password=request.form.get("passwor")
        if((admin==ads)and(password==passwordc)):
            return render_template('article.html')

        
    return render_template('login.html')

@app.route('/articleadd',methods=['POST'])
def articleadd():
    headline=request.form.get("headline")
    intro=request.form.get("intro")
    print(intro)
    return render_template('articleadd.html',headline=headline,intro=intro)


if __name__ == "__main__":
    app.run(debug=True)