<ul>
{% include "escape_filter.tpl"%}
{%- for item in items %}
    <li>{{ item }}</li>
{%- endfor %}
</ul>