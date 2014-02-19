=============================
{{cookiecutter.project_name}}
=============================

{{cookiecutter.project_short_description}}

Requirements
============

The following packages need to be installed::

    brew install python27 libevent

Or with macports::

    sudo port install python27 libevent

{% if cookiecutter.buildout -%}

Initial Setup for Development
=============================

Bootstrap with python 2.7::

    /path/to/python2.7 bootstrap.py

Run buildout::

    bin/buildout -N
{% endif %}
{% if cookiecutter.supervisor -%}
Start Dev Setup
===============

All needed programs can be started under supervisor control.

Start supervisor::

  ./bin/supervisord

Check the status of the programs::

  ./bin/supervisorctl status
  {% if cookiecutter.pyrest -%}
    {%- if cookiecutter.nginx %}
The API is available at http://localhost:9400
    {% elif cookiecutter.haproxy %}
The API is available at http://localhost:9100
    {% else %}
The frontend app is available at http://localhost:9210
    {%- endif %}

    {%- if cookiecutter.haproxy or cookiecutter.crate or cookiecutter.nginx %}
The local topology of the individual services looks as follows::

        {% if cookiecutter.nginx %}
                +----------------+
                |  nginx (9400)  |
                +----------------+
                         |
                         |
                         v
        {%- endif %}
        {%- if cookiecutter.haproxy %}
                +----------------+
                | haproxy (9100) |
                +----------------+
                   |          |
             +-----+          +------+
             |                       |
             v                       v
      +-------------+         +-------------+
      | app  (9210) |         | app2 (9211) |
      +-------------+         +-------------+
            {%- if cookiecutter.crate %}
             |   |               |   |
             |   +-------------------+
             |                   |   |
             +-------------------+   |
            {%- endif %}
        {%- else %}
                +---------------+
                |    app (9210) |
                +---------------+
            {%- if cookiecutter.crate %}
                   |          |
             +-----+          +------+
            {%- endif %}
        {%- endif -%}
        {%- if cookiecutter.crate %}
             |                       |
             v                       v
      +---------------+       +---------------+
      | crate  (4200) |       | crate2 (4201) |
      +---------------+       +---------------+
    {% endif %}
{% endif %}

For debugging the Pyramid app can be started in the foreground. Take care to
stop the apps in the supervisor controller, then run::

  ./bin/app

  {%- endif %}
        {%- if cookiecutter.crate %}

The crate servers are running on port 4200 and 4201 and the admin interface
is reachable at http://localhost:4200/admin.
        {%- endif %}
        {% if cookiecutter.haproxy %}
The status interface for the HAProxy is available at
http://localhost:9100/__haproxy_stats
        {% endif %}
  {% if cookiecutter.crate %}
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
  {% if cookiecutter.sphinx %}
Generating Documentation
========================

To generate the HTML documentation start this script::

  ./bin/sphinx-html
  {%endif %}
{%- endif %}
