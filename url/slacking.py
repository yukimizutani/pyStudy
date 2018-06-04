import requests
import json


def notify(content, mention=False):
    if mention:
        content = "<!channel>" + content
    requests.post('https://hooks.slack.com/services/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', data=json.dumps({
        'text': content,  # 投稿するテキスト
        'username': u'me',  # 投稿のユーザー名
        'icon_emoji': u':ghost:',  # 投稿のプロフィール画像に入れる絵文字
        'link_names': 1,  # メンションを有効にする
    }))
