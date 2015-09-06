"""
This file contains the backend code for the Pebble-WebSockets interface to Minecraft. It should be run in parallel with leapmotion.py.
"""
import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
import socket

from pymouse import PyMouse
from pykeyboard import PyKeyboard
k = PyKeyboard()
m = PyMouse()

class WSHandler(tornado.websocket.WebSocketHandler): #Adapted from an online WebSocket server in Python
    inventory = 1
    def open(self):
        print 'new connection'

    def on_message(self, message):
        print 'message received:  %s' % message
        # Reverse Message and send it back
        if message == "pebble:up":
            if self.inventory == 9:
                self.inventory = 1
            else:
                self.inventory += 1
            k.tap_key(str(self.inventory))
            self.write_message(str(self.inventory))
        elif message == "pebble:down":
            if self.inventory == 1:
                self.inventory = 9
            else:
                self.inventory -= 1
            k.tap_key(str(self.inventory))
            self.write_message(str(self.inventory))
        elif message == "pebble:select":
            m.click(*m.position())
        elif message == "pebble:longselect":
            m.click(*m.position(), button=2)
        else:
            pass


    def on_close(self):
        print 'connection closed'

    def check_origin(self, origin):
        return True

application = tornado.web.Application([
    (r'/', WSHandler),
])


if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8181)
    myIP = socket.gethostbyname(socket.gethostname())
    print '*** Websocket Server Started at %s***' % myIP
    tornado.ioloop.IOLoop.instance().start()
