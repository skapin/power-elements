#!/usr/bin/env python
# -*- coding: utf-8 -*-

from common.server.flaskutils import flask_log
from server.streaming import Streaming

if __name__ == '__main__':
    streaming_inst = Streaming()
    streaming_inst.start()

    flask_log("====>> Waiting Thread...")
    streaming_inst.join()
    flask_log("====>> Thread joined")
