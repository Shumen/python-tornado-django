#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys
import tornado
from tornado import web, websocket, wsgi, ioloop, httpserver
from tornado.options import options, define, parse_command_line
import django.core.handlers.wsgi
 
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ['DJANGO_SETTINGS_MODULE'] = "settings"
 
define('port', type=int, default=8888)
 
class EchoWebSocket(websocket.WebSocketHandler):
	def open(self):
		print "WebSocket opened"

	def on_message(self, message):
		self.write_message(u"Echo: " + message)

	def on_close(self):
		print "WebSocket closed"

def main():
	parse_command_line()
 
	wsgi_app = tornado.wsgi.WSGIContainer(
		django.core.handlers.wsgi.WSGIHandler())
 
	tornado_app = tornado.web.Application([
		(r'/ws', EchoWebSocket),
		('.*', tornado.web.FallbackHandler, dict(fallback=wsgi_app)),
		])
	server = tornado.httpserver.HTTPServer(tornado_app)
	server.listen(options.port)
	tornado.ioloop.IOLoop.instance().start()
 
if __name__ == '__main__':
	main()

