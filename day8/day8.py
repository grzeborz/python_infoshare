import requests
import csv
import folium


def download_data():
    data_url = "https://raw.githubusercontent.com/infoshareacademy/isa-python12/master/Day8/exercises/airports.csv?token=AGMZVYOFLTW6SJTOMBVPTRS5HCKJ2"

    airports_data = requests.get(data_url)

    csv_data = airports_data.text

    csv_filename = "airports.csv"

    with open(csv_filename, "w") as csv_file:
        csv_file.write(csv_data)
        print("Skończone zapisywanie CSV")

download_data()

map = folium.Map()



with open("airports.csv", "r") as csv_file:
    data = csv.reader(csv_file)
    for airport in data:
        icon = folium.Icon(icon='paper-plane', prefix='fa', color="red")
        point = folium.Marker(location=[airport[5],
                                        airport[6]],
                              popup=airport[1],
                              icon=icon)
        map.add_child(point)

map.save("map.html")