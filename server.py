#!/usr/bin/env python3

from http.server import HTTPServer
from handlers import InkyHandler
from functools import partial
from inky.auto import auto

class InkyOutput():
    def __init__(self):
        self.WIDTH = 400
        self.HEIGHT = 300
    def show(this, image):
        inky_display = auto()
        inky_display.set_image(image)
        inky_display.show()

handler = partial(InkyHandler, InkyOutput)

# start the webserver
server = HTTPServer(('', 8081), handler)
server.serve_forever()
