from flask import Flask
from flask import request
from flask import render_template
from flask import json
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/kenobi')
def hello_kenobi():
    return 'General Kenobi!'

@app.route('/kenobigen')
def kenobigen():
    return r'<img src="https://i.ytimg.com/vi/qLAQCYSi1_4/maxresdefault.jpg">'

@app.route('/method', methods=['GET', 'POST'])
def method():
    if request.method == 'POST':
        return 'Użyto metody POST'
    else:
        return 'Użyto metody GET'

@app.route('/hello/<name>')
def hello_name(name):
    return f'Witaj, {name}!'

@app.route('/calc/<liczba>')
def calc(liczba):
    return f'{int(liczba)+6}'

@app.route('/modulo/<int:liczba>')
def modulo(liczba):
    if liczba % 2 == 0:
        return 'Podzielna przez 2'
    elif liczba % 3 == 0:
        return 'Podzielna przez 3'
    elif liczba % 5 == 0:
        return 'Podzielna przez 5'
    else:
        return 'Nie podzielna przez 2, 3 lub 5'

@app.route('/about/<name>')
def hello(name):
    return render_template('about.html', name=name)

@app.route('/api')
def yesorno():
    response = request.get('https://yesno.wtf/api')
    data = response.json()
    return f'{data['answer']}'