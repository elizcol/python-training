'''
Created on 27 Nov 2014

@author: b8605521
'''
#flask
from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def hello(name=None):
    return 'Hello World.'
    #add templates folder in at same level with template with {{name}}
    #return render_template('template.html', name=name)

if __name__ == '__main__':
    app.run()