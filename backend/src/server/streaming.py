import asyncio
import websockets
import signal
import json
import datetime
import cv2
import numpy as np

from threading import Thread, RLock
from common.server.flaskutils import flask_log
from image_processing.strike_checker import StrikeChecker

strike_zone_checker = StrikeChecker()

def parse_image_size(size_msg):
    w, h = map(int, size_msg.split('x'))
    return (w, h)

async def handle_client_message(websocket, path):
    global strike_zone_checker
    while True:
        try:
            # receive image
            jpg_img = await websocket.recv()
            # decompress it
            # rgb_img = cv2.imdecode(np.frombuffer(jpg_img, dtype=np.uint8), 1)
            # process it
            striked_out = strike_zone_checker.check(jpg_img)
            if striked_out:
                await websocket.send('Out')
            else:
                await websocket.send('In')

        except websockets.ConnectionClosed:
            flask_log("===> WebSocket Closed")
            # Connection lost, reinitialize background model
            strike_zone_checker = StrikeChecker()
            return

class Streaming(Thread):
    def __init__(self, host='0.0.0.0', port=9988):
        Thread.__init__(self)
        self.port = port
        self.host = host
        flask_log('===> Streaming Thread init')

    def run(self):
        flask_log('===> Streaming Thread Starting')

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        try:
            web_socket = websockets.serve(handle_client_message, self.host, self.port)
            asyncio.get_event_loop().run_until_complete(web_socket)
            asyncio.get_event_loop().run_forever()
            flask_log('===> Run Forever ended')

        except Exception as e:
            flask_log('____error on streaming   _____')
            flask_log(str(e))
            raise e
        flask_log('== Stopped')
