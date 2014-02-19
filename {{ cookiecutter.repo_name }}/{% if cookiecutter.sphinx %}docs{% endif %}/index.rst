=============================
{{cookiecutter.project_name}}
=============================

{{cookiecutter.project_short_description}}

Contents:
---------

{% if cookiecutter.pyrest %}
.. toctree::
   :maxdepth: 2
   :titlesonly:

   reference.rst
{% endif %}
