import requests, json
from subprocess import call
from bs4 import BeautifulSoup

### TIVA ###
url = 'https://tivahq.com/covid19/py/data'
r = requests.get(url)
data = r.text

data = data.replace('test:', '"test":')

with open('data.json', 'w') as f:
    f.write(data)

### WO ###
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


### PUSH TO GITHUB ###
#Commit Message
commit_message = "Adding sample files"

#Stage the file
#call('cd /home/pi/Documents/covid/covid-data', shell = True)
call('git add .', shell = True)

# Add your commit
call('git commit -m "'+ commit_message +'"', shell = True)

#Push the new or update files
call('git push origin master', shell = True)
