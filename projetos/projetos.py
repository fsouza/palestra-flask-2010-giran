#coding:utf-8
from flask import Flask, render_template, redirect, url_for
from flaskext.sqlalchemy import SQLAlchemy
from flaskext import wtf

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dados.sqlite3'
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
    if formulario.validate_on_submit():
        projeto = Projeto()
        projeto.nome = formulario.nome.data
        projeto.descricao = formulario.descricao.data
        db.session.add(projeto)
        db.session.commit()
        return redirect(url_for('listar_projetos'))
    return render_template('novo_projeto.html', form=formulario)

@app.route('/projetos')
def listar_projetos():
    projetos = Projeto.query.all()
    return render_template('projetos.html', projetos=projetos)

if __name__ == '__main__':
    db.create_all()
    app.run()
