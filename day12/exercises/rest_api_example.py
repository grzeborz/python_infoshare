import requests
#import json
#http://www.recipepuppy.com/api/?i=onions,garlic&q=omelet&p=3

response = requests.get('http://www.recipepuppy.com/api/', params={'i':'onions,garlic', 'q':'omelet', 'p':'1'})

print(response)

print(response.status_code)

recipes = response.json()['results']


for recipe in recipes:
    print("\n")
    print(recipe['title'])
    print(30* '-')
    print(recipe['ingredients'])