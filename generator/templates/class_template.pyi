{{'# ' + "=" * (notice.__len__() + 6) + " #"}}
{{'# ' + " " * (notice.__len__() + 6) + " #"}}
#    {{ notice }}    #
{{'# ' + " " * (notice.__len__() + 6) + " #"}}
{{'# ' + "=" * (notice.__len__() + 6) + " #"}}
from __future__ import annotations

{ %
for d in entity.dependencies -%}
from

{ % if entity.is_function %}..types
{ % else %}.{{d.name}}
{ % endif %} import

{{d.type}}
{ % endfor - %}

{ %
import

'base_class_template.pyi' as base_class %}
{{base_class.


class(entity) }}

{% - for subclass in entity.subclasses %}
{{base_class.class (subclass, entity.uf_name)}}
{% endfor %}

{% - for dep in entity.cross_deps %}
{{base_class.class (dep)}}
{% endfor %}
