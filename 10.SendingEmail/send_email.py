# send an email with the contnent from the API (https://v2.jokeapi.dev/)
# implement logging
# make sure that email creds are not in teh script (external JSON file)
# PROPERLY handle all exceptions specifically


import requests

url = "https://v2.jokeapi.dev/joke/Programming?blacklistFlags=nsfw,religious,political,racist,sexist,explicit"

response = requests.get(url)

result = response.json()

print(result)
