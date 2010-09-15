from flask import Flask

app = Flask('hello')

@app.route('/hello')
def hello():
    return 'Hello world'

app.run()
