{# childe.tpl 子テンプレート #}

{% extends "base/base.tpl" %} {# 親テンプレートを指定 #}

{% block title %}{{contentType}}{% endblock %}

{% block content %}
{% include "top_content/notification.tpl" %}
 {% if contentType == "shop" %}
<div class="content">
{% include "shop_content/shop_content.tpl" %}
</div>
{% elif contentType == "code" %}
<div class="content">
{% include "code_content/code_content.tpl" %}
</div>
{% elif contentType == "trade" %}
<div class="content">
{% include "trade_content/trade_content.tpl" %}
</div>
{% elif contentType == "myPage" %}
<div class="content">
{% include "mypage_content/mypage_content.tpl" %}
</div>
{% else %}
<div class="content">
{% include "top_content/top_content.tpl" %}
</div>
{% endif %}
<style type="text/css">
.content {
    position: relative;
    display: block;
    border: 5px;
}

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