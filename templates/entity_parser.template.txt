{% macro getattr(x, n) %}{{ x[n] }}{% endmacro %}
{% macro def_attr(p) %}'{{ p.name }}': self.{{ p.name }}{% endmacro %}

{% set parent = subtype_of if subtype_of != None else "IfcEntity" %}
{% set attrs = clauses["DECLARATION"] %}

{% if is_abstract %}
@ifc_abstract_class
{% else %}
@ifc_class
{% endif %}
class {{ defname }}({{ parent }}):
    def __init__(self, rtype, args):
        {{ parent }}.__init__(self, rtype, args)
        {% for attr in attrs %}
        {% if attr.value == "IfcGloballyUniqueId" %}
        self.{{ attr.name }} = parse_uuid(args.pop())
        {% else %}
        self.{{ attr.name }} = args.pop()
        {% endif %}
        {% endfor %}

    def __str__(self):
        return "{sup}
{%- for attr in attrs -%}
:{{ attr.name + ':{' + attr.name + '}' }}
{%- endfor -%}".format(
                sup={{ parent }}.__str__(self),
                {% for attr in attrs %}
                {{ attr.name }}=self.{{ attr.name }},
                {% endfor %}
                )

    def __json__(self):
        sup = {{ parent }}.__json__(self)
        attrs = { {{ attrs | apply(def_attr) | join(', ') }} }
        res = {'rtype': self.rtype }
        res.update(sup)
        res.update(attrs)
        return res


{# vim: set sw=4 ts=4 et: #}
