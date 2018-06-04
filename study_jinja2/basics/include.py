from jinja2 import Template, Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('/home/yuki/PycharmProjects/pyStudy/study_jinja2/basics'))
template = env.get_template('include.tpl')


def include_template():
    data = {'items': ['みかん', 'りんご', 'バナナ']}
    disp_text = template.render(data)
    return (disp_text)
