from jinja2 import Template, Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('.'))
env.line_statement_prefix = '#'
template = env.get_template('line_statement.tpl')
data = {'items': ['みかん', 'りんご', '<バナナ>']}
disp_text = template.render(data)
print(disp_text)