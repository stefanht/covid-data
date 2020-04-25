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

data = {}

for c in start:
    # 11 es test/1Mpop
    data[search[c].get_text()] = int(search[c+11].get_text().replace(',', ''))

sorted_data = sorted(data.items(), key=lambda x: x[1], reverse=True)    

with open("wo-tests.json", "w") as f:
    f.write('[')
    for i in range(len(sorted_data)):
        f.write('{"country":"'+sorted_data[i][0] + '","tests":' + str(sorted_data[i][1]) + '}')
        if i+1 != len(sorted_data):
            f.write(',')
    f.write(']')