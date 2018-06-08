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
{% else %}
{% elif contentType == "myPage" %}
<div class="content">
{% include "trade_content/trade_content.tpl" %}
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
</style>