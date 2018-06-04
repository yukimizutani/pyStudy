from jinja2 import Template, Environment, FileSystemLoader


def get_template():
    env = Environment(loader=FileSystemLoader('/home/yuki/PycharmProjects/pyStudy/study_jinja2/basics'), trim_blocks=False)
    template = env.get_template('child.tpl')
    disp_text = template.render()
    return disp_text
