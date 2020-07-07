from flask import Flask, request, url_for,render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import os
from sqlalchemy.orm.attributes import flag_modified
UPLOAD_FOLDER = './static/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif','doc'}

app = Flask(__name__)
app.secret_key="12345678"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///db.sqlite3'#DBURI
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

db=SQLAlchemy(app)
#articles=db.Table('articles',db.metadata,autoload=True,autoload_with=db.engine,extend_existing=True)

class articles(db.Model):
    ID=db.Column('ID',db.Integer,primary_key=True, autoincrement=True)
    headline=db.Column('headline',db.Text)
    intro=db.Column('intro',db.Text)
    loc1=db.Column('loc1',db.Text)
    loc2=db.Column('loc2',db.Text)
    afterimg=db.Column('afterimg',db.Text)
    cardtext=db.Column('cardtext',db.Text)
    field=db.Column('field',db.Text)
    level=db.Column('level',db.Text)
    def _init_(self,ID,headline,intro,loc1,loc2,afterimg,cardtext,field,level):
        self.ID=ID
        self.headline=headline
        self.intro=intro
        self.loc1=loc1
        self.loc2=loc2
        self.afterimg=afterimg
        self.cardtext=cardtext
        self.field=field
        self.level=level
     

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
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
    article = articles.query.filter_by(field="blockchain")
    return render_template('blockchain.html', articles = article)

@app.route('/webdev')
def webdev():
    article = articles.query.filter_by(field="webdev")
    return render_template('webdev.html', articles = article)


@app.route('/appdev')
def appdev():
    article = articles.query.filter_by(field="appdev")
    return render_template('appdev.html', articles = article)

@app.route('/aiml')
def aiml():
    article = articles.query.filter_by(field="aiml")
    return render_template('aimln.html', articles = article)


@app.route('/iot')
def iot():
    article = articles.query.filter_by(field="iot")
    return render_template('iot.html', articles = article)


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

@app.route('/addarticle',methods=['POST'])
def addarticle():
    if request.method == 'POST':
        if 'img1' not in request.files:
            return render_template('APIs.html')
        if 'img2' not in request.files:
            return render_template('aiml.html')
            
        img1 = request.files['img1']
            
        if img1.filename == '':
            return render_template('webdev.html')
            
        if img1 and allowed_file(img1.filename) :
            filename = secure_filename(img1.filename)
            img1.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            loc1=os.path.join(app.config['UPLOAD_FOLDER'], filename)
        
        img2 = request.files['img2']
            
        if img2.filename == '':
            return render_template('appdev.html')
            
        if img2 and allowed_file(img2.filename) :
            filename = secure_filename(img2.filename)
            img2.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            loc2=os.path.join(app.config['UPLOAD_FOLDER'], filename)


        headline=request.form.get("headline")
        intro=request.form.get("intro")
        afterimg=request.form.get("afterimg")
        cardtext=request.form.get("cardtext")
        field=request.form.get("field")
        level=request.form.get("level")
        article=articles(headline=headline,intro=intro,loc1=loc1,loc2=loc2,afterimg=afterimg,cardtext=cardtext,field=field,level=level)
        db.session.add(article)
        db.session.commit()
        #print(intro)
    return render_template('articleadd.html',headline=headline,intro=intro,loc1=loc1,loc2=loc2,afterimg=afterimg)


@app.route("/<int:ID>")
def post(ID):
    article = articles.query.get_or_404(ID)
    return render_template("editarticle.html", ID=article.ID, headline=article.headline, intro=article.intro, img1=article.loc1, img2=article.loc2)

if __name__ == "__main__":
    app.run(debug=True)