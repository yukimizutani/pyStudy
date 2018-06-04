from jinja2 import Template, Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('.'), trim_blocks=False)
template = env.get_template('escape_filter.tpl')

data = {'items': ['<みかん>', '<りんご>', '<バナナ オーレ>']}
disp_text = template.render(data)
print(disp_text)