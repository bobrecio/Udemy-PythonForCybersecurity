

import requests

url = 'https://reddit.com'


h = {
    'User-agent': 'Googlebot'
}

response = requests.get(
    url,
    headers=h
)


print(response.text)
