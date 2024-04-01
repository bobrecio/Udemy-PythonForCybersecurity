from urllib import response
import requests
import json

base_url = 'https://www.thecocktaildb.com/api/json/v1/1/search.php?s='
query = input("Please enter a drink to search >> ")

r = requests.get(f'{base_url}{query}')

print(r.json())

result = r.json()['drinks']
instructions = result[0]['strInstructions']
print(f"instructions: {instructions}")
