{# include.tpl #}

{% include "nav.tpl" %}
<div class="content">
    <ul>
        {% for item in items -%}
        <li>{{ item}}</li>
        {% endfor %}
    </ul>
</div>