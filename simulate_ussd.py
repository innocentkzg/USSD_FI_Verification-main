# simulate_ussd.py

import requests

def simulate_ussd():
    url = 'http://127.0.0.1:8000/api/ussd/'
    payload = {
        'text': ''  # Initial request text
    }

    # Initial request
    response = requests.post(url, data=payload)
    print('Response:', response.text)

    # Simulate entering option 1
    payload['text'] = '1'
    response = requests.post(url, data=payload)
    print('Response:', response.text)

    # Simulate entering an institution code
    payload['text'] = '1*1234'
    response = requests.post(url, data=payload)
    print('Response:', response.text)

if __name__ == '__main__':
    simulate_ussd()
