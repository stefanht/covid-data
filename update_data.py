import requests, json
from collections import OrderedDict
from subprocess import call
from csv import reader, writer

url = 'https://tivahq.com/covid19/py/data'
r = requests.get(url)
data = r.json(object_pairs_hook=OrderedDict)
#print(data)

data = data['data']['data']
tests = 0
for k,v in data.items():
    if 'mobility' in v: 
        del v['mobility']
    if 'source' in v: 
        del v['source']
    tests = tests + v['analyzed']
    v.update({'tests':tests})


with open('output', 'w') as f:
    f.write('Fecha,Analizados,Positivos,Importados,Relacionados,Confirmados,Fallecidos,Recuperados,Hospitalizados,Tests')
    f.write('\n')
    for k,v in data.items():
        #print('"'+k+'"', end='')
        if v['analyzed'] == 0:
            continue
        f.write('"'+k+'"')
        for k1,v1 in v.items():
            f.write(',"'+str(v1)+'"')
        f.write('\n')

#with open('output') as f, open('output_tr', 'w') as fw: 
#    writer(fw, delimiter=',').writerows(zip(*reader(f, delimiter=',')))

#Commit Message
commit_message = "Adding sample files"

#Stage the file
#call('cd /home/pi/Documents/covid/covid-data', shell = True)
call('git add .', shell = True)

# Add your commit
call('git commit -m "'+ commit_message +'"', shell = True)

#Push the new or update files
call('git push origin master', shell = True)

