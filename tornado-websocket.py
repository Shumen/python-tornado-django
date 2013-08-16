#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys
import tornado
from tornado import ioloop, web, websocket, httpserver

class EchoWebSocket(tornado.websocket.WebSocketHandler):
	def open(self):
		print "WebSocket opened"

	def on_message(self, message):
		self.write_message(u"Echo: " + message)

	def on_close(self):
		print "WebSocket closed"

application = tornado.web.Application([
	(r'/', EchoWebSocket),
])

if __name__ == '__main__':
	http_server = tornado.httpserver.HTTPServer(application)
	http_server.listen(8888)
	tornado.ioloop.IOLoop.instance().start()

# test example
#ws = new WebSocket("ws://localhost:8888", "echo");
#ws.onmessage=function(evt) { console.log(evt.data); }
#ws.send("hi");
#ws.close();

