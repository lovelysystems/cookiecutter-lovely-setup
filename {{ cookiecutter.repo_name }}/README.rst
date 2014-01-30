=============================
{{cookiecutter.project_name}}
=============================

{{cookiecutter.project_short_description}}

{% if cookiecutter.buildout.startswith('y') -%}

Initial Setup for Development
=============================

Bootstrap with python 2.7::

    /path/to/python2.7 bootstrap.py

Run buildout::

    bin/buildout -N
{% endif %}
{% if cookiecutter.supervisor.startswith('y') -%}
Start Dev Setup
===============

All needed programs can be started under supervisor control.

Start supervisor::

  ./bin/supervisord

Check the status of the programs::

  ./bin/supervisorctl status

  {% if cookiecutter.pyrest -%}
The frontend app is available at http://localhost:8200

For debugging the Pyramid app can be started in the foreground. Take care to
stop the apps in the supervisor controller, then run::

  ./bin/app

  {%- endif %}
  {% if cookiecutter.crate.startswith('y') %}
Setup crate database
--------------------

To initialize a empty crate database run the command

  $ bin/crate_setup

If the database has been setup already the script will raise an error but no
data will get destroyed.

Clean up crate database
-----------------------

To reset the crate database to it's initial state run the command

  $ bin/crate_cleanup

CAUTION: This command will delete all data!
  {%-endif %}
  {% if cookiecutter.sphinx.startswith('y') %}
Generating Documentation
========================

To generate the HTML documentation start this script::

  ./bin/sphinx-html
  {%endif %}
{%- endif %}
