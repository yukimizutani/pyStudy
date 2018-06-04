{# base.tpl baseテンプレート #}
<!DOCTYPE html>
<html lang="ja">
    <head>
        <!-- 共通ヘッダ -->
        {% block head %}
        <link rel="stylesheet" href="/static/css/base.css" type="text/css" />
        <title>{% block title %}{% endblock %} - チャンコーデ</title>
        {% endblock %}
        <script>
          function show(plugin) {
              console.log(plugin);
            }
        </script>
    </head>
    <body>
        <!-- ツールバー -->
        <div id="toolbar">
            {% block toolbar %}
            {% include "toolbar.tpl" %}
            {% endblock %}
        </div>

        <!-- コンテンツ部分 -->
        <div id="content">
            {% block content %}
            {% include "content.tpl" %}
            {% endblock %}
        </div>

        <!-- 共通フッター -->
        <div id="footer">
            {% block footer %}
            {% include "footer.tpl" %}
            {% endblock %}
        </div>
    </body>
</html>