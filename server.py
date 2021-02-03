"""

"""

from flask import Flask, render_template, request
import time

server = Flask(__name__)

messages = [
    {'username': 'dim-akim', 'text': 'Здравствуйте!', 'timestamp': time.time()},
    {'username': 'fomin-k', 'text': 'Добрый день!', 'timestamp': time.time()},
    {'username': 'kaleda-s', 'text': 'И вам не хворать!', 'timestamp': time.time()}
]

@server.route('/')
def hello():
    return '''Hello, World!
    <br>
    <a target="_blank" href="index">index</a>'''


@server.route('/get_messages')
def get_messages():
    after = float(request.args['after'])

    result = []
    for message in messages:
        if message['timestamp'] > after:
            result.append(message)
    return {
        'messages': result
    }


@server.route('/send_messages') # открытия дорожки
def send_messages():

    messages.append(
        {
            'username': request.json['username'],
            'text': request.json['text'],
            'timestamp': time.time()
        }
    )


@server.route('/index')
def index():
    name = 'Дмитрий Валерьевич'
    return render_template('index.html')


server.run()