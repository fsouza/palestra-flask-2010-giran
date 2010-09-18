#coding:utf-8
from flask import Flask, render_template
from flaskext.sqlalchemy import SQLAlchemy
from flaskext import wtf

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SECRET_KEY'] = 'HSAOIHs8ashw8JSJ'
app.config['CSRF_ENABLED'] = True
app.config['CSRF_SESSION_KEY'] = 'HSAOIHs8ashw8JSJwtforms'
db = SQLAlchemy(app)

class Projeto(db.Model):
    __tablename__ = 'projetos'
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100), nullable = False)
    descricao = db.Column(db.Text, nullable = False)

class ProjetoForm(wtf.Form):
    nome = wtf.TextField(u'Nome', validators=[wtf.Required()])
    descricao = wtf.TextAreaField(u'Descrição', validators=[wtf.Required()])

@app.route('/novo_projeto', methods=['GET', 'POST'])
def novo_projeto():
    formulario = ProjetoForm()
    return render_template('novo_projeto.html', form=formulario)

app.run()
