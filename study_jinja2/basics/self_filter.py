from jinja2 import Template, Environment, FileSystemLoader


def sample(arg):
    """ 引数をアスタリスクで装飾した文字列を返す """
    return "*** " + str(arg) + " ***"


env = Environment(loader=FileSystemLoader('.'), trim_blocks=False)

# 自作フィルタを設定する
env.filters['sample_filter'] = sample
template = env.get_template('self_filter.tpl')

data = {'items': ['みかん', 'りんご', 'バナナ']}
disp_text = template.render(data)
print(disp_text)
