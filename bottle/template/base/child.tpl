{# childe.tpl 子テンプレート #}

{% extends "base/base.tpl" %} {# 親テンプレートを指定 #}

{% block title %}Index{% endblock %}

{% block head %}
    {{ super() }}
{% endblock %}