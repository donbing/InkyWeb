import threading
import time
import unittest
from http.server import HTTPServer
from urllib import request
from handlers import InkyHandler
from functools import partial


class FakeOutput():
    def __init__(self):
        self.WIDTH = 400
        self.HEIGHT = 300
    def show(self, image):
        self.last_image = image


class TestRequests(unittest.TestCase):

    def setUp(self):
        self.server = None
        self.port = 21344
        self.host = ''
        self.start_server()

    def start_server(self):
        self.output = FakeOutput()
        partial_handler = partial(InkyHandler, self.output)
        self.server = HTTPServer((self.host, self.port), partial_handler)
        self.server_thread = threading.Thread(target=self.server.serve_forever)
        self.server_thread.daemon = True
        self.server_thread.start()
        time.sleep(0.25)

    def stop_server(self):
        if self.server is None:
            return
        self.server.shutdown()
        self.server_thread.join()

    def tearDown(self):
        self.stop_server()

    def test_get(self):
        req = request.Request(f"http://localhost:{self.port}/")
        req.add_header('accept', 'application/json')
        response = request.urlopen(req).read()
        print(response)
    
    def test_post(self):
        req = request.Request(f"http://localhost:{self.port}/", method='POST')
        req.add_header('accept', 'application/json')
        response = request.urlopen(req).read()
        print(response)


if(__name__ == '__main__'):
    unittest.main()
