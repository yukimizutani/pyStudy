{% include "escape_filter.tpl"%}
<ul>
{%- for item in items %}
    <li>{{ item }}</li>
{%- endfor %}
</ul>