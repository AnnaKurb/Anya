import requests


response = requests.get('http://127.0.0.1:5000/get_messages')

for message in response.json()['messages']:
    print(f'{message["username"]}: "{message["text"]}"')