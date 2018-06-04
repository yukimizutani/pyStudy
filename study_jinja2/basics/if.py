from jinja2 import Template, Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('if.tpl')

data = {'x': 0}
disp_text = template.render(data)
print(disp_text)