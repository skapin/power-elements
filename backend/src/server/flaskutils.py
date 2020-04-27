from __future__ import print_function

import sys
import logging
import requests

from flask import request, abort
from logging.handlers import RotatingFileHandler
from config.settings import SETTINGS


def init_logging():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG if SETTINGS['DEBUG_MODE'] else logging.WARNING)

    # in file
    formatter = logging.Formatter(
        "%%(levelname)s: %%(asctime)-15s %s[%%(process)d]: %%(message)s" % __name__, datefmt='%Y-%m-%d %H:%M:%S')
    # file_handler = RotatingFileHandler('activity.log', 'a', 1000000, 1)
    # file_handler.setLevel(logging.DEBUG)
    # file_handler.setFormatter(formatter)
    # logger.addHandler(file_handler)

    # in console
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)
    # stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    logger.info('> Logging Module initialized')


def print_flush(msg):
    print(msg, file=sys.stderr)
    sys.stderr.flush()


def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()


def abort_doesnt_exist(obj):
    if not obj:
        abort(404, message="Object doesn't exist")


def call(method, url, params=None, headers=None, **kwargs):
    req_headers = dict()
    if headers:
        req_headers.update(headers)
    return requests.request(method=method, url=url, params=params, headers=req_headers, **kwargs)


def is_status_ok(status):
    return 200 <= status < 300
