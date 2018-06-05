<div class="notification">
<div>重要なお知らせ</div>
{% block notification %}
{% include "top_content/notification.tpl" %}
{% endblock %}
</div>
<div class="news">
<div>お知らせ</div>
{% block news %}
{% include "top_content/news.tpl" %}
{% endblock %}
</div>
<div class="description">
<div>サイトの説明</div>
{% block description %}
{% include "top_content/description.tpl" %}
{% endblock %}
</div>
<style type="text/css">
.notification {
    position: relative;
    display: block;
    border: 1px dotted gray;
}
.news {
    position: relative;
    display: block;
    border: 1px dotted gray;
}
.description {
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