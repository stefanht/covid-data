import os
import jinja2
from subprocess import call

with open("output", "r") as file:
    for last_line in file:
        pass

last_line = last_line.replace('"','')
last_line = last_line.split(',')

confirmed = int(last_line[5])
deceased = int(last_line[6])
recovered = int(last_line[7])
tested = int(last_line[-1])

template_filename = "./template.html"
rendered_filename = "index.html"
render_vars = {
    "confirmed": confirmed,
    "deceased": deceased,
    "recovered": recovered,
    "active": confirmed - deceased - recovered,
    "tested": tested
}

script_path = os.path.dirname(os.path.abspath(__file__))
template_file_path = os.path.join(script_path, template_filename)
rendered_file_path = os.path.join(script_path, rendered_filename)

environment = jinja2.Environment(loader=jinja2.FileSystemLoader(script_path))
output_text = environment.get_template(template_filename).render(render_vars)

with open(rendered_file_path, "w") as result_file:
    result_file.write(output_text) 

call('surge .', shell = True)
