from flask import Flask, render_template,request, url_for
from flask_sqlalchemy import SQLAlchemy
import psycopg2
from sqlalchemy.orm.attributes import flag_modified

app = Flask(__name__)
app.secret_key="12345678"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://nik:password@localhost/datatest'#dburi
db=SQLAlchemy(app)
articles=db.Table('articles',db.metadata,autoload=True,autoload_with=db.engine,extend_existing=True)

class articles(db.Model):
    _tablename_='articles'
    __table_args__ = {'extend_existing': True} 
    id=db.Column('id',db.Integer,primary_key=True)
    headline=db.Column('headline',db.Text)
    intro=db.Column('intro',db.Text)
    #entries=db.Column('entries',db.Integer)
    def _init_(self,id,headline,intro):
        self.id=id
        self.headline=headline
        self.intro=intro


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
    article=articles(headline=headline,intro=intro)
    db.session.add(article)
    db.session.commit()
    #print(intro)
    return render_template('articleadd.html',headline=headline,intro=intro)


if __name__ == "__main__":
    app.run(debug=True)