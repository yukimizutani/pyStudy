{# childe.tpl 子テンプレート #}

{% extends "base/base.tpl" %} {# 親テンプレートを指定 #}

{% block title %}{{contentType}}{% endblock %}

{% block content %}
<!--{% include "top_content/notification.tpl" %}-->
{{ childElem }}
<style type="text/css">
.content {
    position: relative;
    display: block;
    border: 5px;
}l

.notification {
    position: relative;
    display: block;
    border: 1px dotted gray;
}

#message {
    position: relative;
    display: block;
    height: 100px;
    border: 5px double;
    margin: 5px;
}
</style>
{% endblock %}