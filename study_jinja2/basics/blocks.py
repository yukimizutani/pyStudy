from jinja2 import Template, Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('blocks.tpl')
data = {'items': ['みかん', 'りんご', '<バナナ>']}
disp_text = template.render(data)
print(disp_text)