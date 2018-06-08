{# base.tpl baseテンプレート #}
<!DOCTYPE html>
<html lang="ja">
    <head>
        <!-- 共通ヘッダ -->
        {% block head %}
        <title>{% block title %}{% endblock %} - チャンコーデ</title>
        {% endblock %}
        <script>
          function show(plugin) {
              console.log(plugin);
            }
        </script>
        <link rel="stylesheet" href="/static/css/base.css" type="text/css" />
    </head>
    <body>
        <!-- ツールバー -->
        <div id="toolbar">
            {% include "toolbar/toolbar.tpl" %}
        </div>

        <!-- コンテンツ部分 -->
        <div id="content">
            {% block content %}
            {% endblock %}
        </div>

        <!-- 共通フッター -->
        <div id="footer">
            {% block footer %}
            {% include "footer/footer.tpl" %}
            {% endblock %}
        </div>
    </body>
</html>