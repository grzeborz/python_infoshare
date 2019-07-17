import requests

data_url = "https://raw.githubusercontent.com/infoshareacademy/isa-python12/master/Day8/exercises/airports.csv?token=AGMZVYOFLTW6SJTOMBVPTRS5HCKJ2"

airports_data = requests.get(data_url)

print(airports_data.content)