from pyramid.view import view_config
from pyramid.response import Response


@view_config(route_name='probe_status')
def probe_status_view(request):
    response = Response("OK")
    response.content_type = 'text/plain'
    return response


def includeme(config):
    config.add_route("probe_status", "/probe_status")
