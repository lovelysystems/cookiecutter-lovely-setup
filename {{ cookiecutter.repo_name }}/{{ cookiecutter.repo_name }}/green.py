from gevent.pywsgi import WSGIServer, WSGIHandler


class LoggingWSGIHandler(WSGIHandler):

    def log_request(self):
        # do not log each request
        pass


def server_factory(global_conf, host, port):
    """Provide the WSGI server for paste

    This must be setup as the paste.server_factory in the egg entry-points.
    """
    port = int(port)

    def serve(app):
        WSGIServer(
            (host, port),
            app,
            handler_class=LoggingWSGIHandler,
        ).serve_forever()
    return serve
