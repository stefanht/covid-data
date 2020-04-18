import os
import jinja2
from subprocess import call

with open("output", "r") as file:
    #for last_line in file:
        #pass
    lines = file.read().splitlines()
    last_line = lines[-1]
    last_line_2 = lines[-2]

last_line = last_line.replace('"','')
last_line = last_line.split(',')

last_line_2 = last_line_2.replace('"','')
last_line_2 = last_line_2.split(',')

positive = int(last_line[2])
confirmed = int(last_line[5])
deceased = int(last_line[6])
recovered = int(last_line[7])
tested = int(last_line[9])
active = int(last_line[10])

active_daily = active - int(last_line_2[10])
active_perc = round(active_daily / active * 100, 2)

positive_inc = round(positive / confirmed * 100, 2)
test_popu = round(tested / 7000000 * 100, 2)

death_perc = round(deceased / confirmed * 100, 2)
recovered_perc = round(recovered / confirmed * 100, 2)

template_filename = "./template.html"
rendered_filename = "index.html"
render_vars = {
    "positive": positive,
    "positive_inc": positive_inc,
    "confirmed": confirmed,
    "deceased": deceased,
    "recovered": recovered,
    "active": active,
    "tested": tested,
    "test_popu": test_popu,
    "death_perc": death_perc,
    "recovered_perc": recovered_perc,
    "active_daily": active_daily,
    "active_perc": active_perc
}

script_path = os.path.dirname(os.path.abspath(__file__))
template_file_path = os.path.join(script_path, template_filename)
rendered_file_path = os.path.join(script_path, rendered_filename)

environment = jinja2.Environment(loader=jinja2.FileSystemLoader(script_path))
output_text = environment.get_template(template_filename).render(render_vars)

with open(rendered_file_path, "w") as result_file:
    result_file.write(output_text) 

#call('surge .', shell = True)
