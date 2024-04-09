# send an email with the contnent from the API (https://v2.jokeapi.dev/)
# implement logging
# make sure that email creds are not in teh script (external JSON file)
# PROPERLY handle all exceptions specifically


import requests

url = "https://v2.jokeapi.dev/joke/Programming?blacklistFlags=nsfw,religious,political,racist,sexist,explicit"

def get_joke_content():
    response = requests.get(url)
    result = response.json()
    if result['error']:
        return None
    if result['type'] == 'twopart':
        setup = result['setup']
        delivery = result['delivery']
        return f"Setup: {setup}\nDelivery: {delivery}"
    else:
        joke = result['joke']
        return f"Joke: {joke}"

print(get_joke_content())