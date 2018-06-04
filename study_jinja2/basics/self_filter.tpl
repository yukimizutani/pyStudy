{# sample.tpl #}
<ul>
    {% for item in items -%}
    <li>{{ item | sample_filter}}</li>
    {% endfor %}
</ul>