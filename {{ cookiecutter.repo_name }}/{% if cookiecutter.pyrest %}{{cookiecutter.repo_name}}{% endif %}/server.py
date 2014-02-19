from pyramid.config import Configurator
{%- if cookiecutter.crate %}
from pyramid.settings import aslist, asbool
from sqlalchemy import create_engine
from .model import DBSession, Base
{%- endif %}


def app_factory(global_config, **settings):
    """Setup the main application for paste

    This must be setup as the paste.app_factory in the egg entry-points.
    """
    config = Configurator(settings=settings, autocommit=True)
    config.include('{{cookiecutter.repo_name}}.probestatus.view')
    config.scan('{{cookiecutter.repo_name}}.probestatus')
{%- if cookiecutter.crate %}
    crate_init(config)
{%- endif %}
    return config.make_wsgi_app()

{% if cookiecutter.crate %}
def crate_init(config):
    settings = config.get_settings()
    engine = create_engine(
        'crate://',
        connect_args={
            'servers': aslist(settings['crate.hosts'])
        },
        echo=asbool(settings.get('crate.echo', 'False')),
        pool_size=int(settings.get('sql.pool_size', 5)),
        max_overflow=int(settings.get('sql.max_overflow', 5))
    )
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
{%- endif -%}
