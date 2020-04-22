import requests, json
from subprocess import call

url = 'https://tivahq.com/covid19/py/data'
r = requests.get(url)
data = r.text
#print(data)

with open('data.json', 'w') as f:
    f.write(data)

#Commit Message
commit_message = "Adding sample files"

#Stage the file
#call('cd /home/pi/Documents/covid/covid-data', shell = True)
call('git add .', shell = True)

# Add your commit
call('git commit -m "'+ commit_message +'"', shell = True)

#Push the new or update files
call('git push origin master', shell = True)
