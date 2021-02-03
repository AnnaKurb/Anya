import requests


username = input('Твое имя: ')

while True:
    text = input('Введи текст сообщения: ')


    requests.get(
        'http://127.0.0.1:5000/send_messages',
        json={'username': username, 'text': text}
    )
