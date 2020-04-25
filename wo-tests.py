from bs4 import BeautifulSoup
import requests

country = ["Paraguay", "USA", "Slovenia", "Italy", "S. Korea", "Germany", "Brazil", "Ecuador", "Argentina", "Uruguay", "Chile"]
worldmetersLink = "https://www.worldometers.info/coronavirus/"

try:
    html_page = requests.get(worldmetersLink)
except requests.exceptions.RequestException as e: 
    print(e) #ConnectionError
bs = BeautifulSoup(html_page.content, 'html.parser')


search = bs.select("#main_table_countries_today tbody tr td")
start = []
for i in range(len(search)):
    if search[i].get_text() in country:
        start.append(i)

countries = []
data = []

for c in start:
    try:
        # 11 es test/1Mpop
        countries.append(search[c].get_text())
        data = data + [search[c+11].get_text().replace(',', '')]
    except:
        countries = countries + ["0"]
        data = data + ["0"]

with open("wo-tests.json", "w") as f:
    f.write('[')
    for i in range(len(countries)):
        f.write('{"country":"'+countries[i] + '","tests":' + data[i] + '}')
        if i+1 != len(countries):
            f.write(',')
    f.write(']')