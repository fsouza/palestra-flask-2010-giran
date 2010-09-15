from flask import Flask
from flaskext.sqlalchemy import SQLAlchemy
from flaskext import wtf

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
db = SQLAlchemy(app)

class Projeto(db.Model):
    __tablename__ = 'projetos'
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100), nullable = False)
    descricao = db.Column(db.Text, nullable = False)

class ProjetoForm(wtf.Form):
    nome = wtf.TextField('Nome', validators=[wtf.Required()])
    descricao = wtf.TextAreaField('Descrição', validators=[wtf.Required()])

app.run()
