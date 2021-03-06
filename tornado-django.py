#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys
import tornado
from tornado import web, wsgi, ioloop, httpserver
from tornado.options import options, define, parse_command_line
import django.core.handlers.wsgi
 
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ['DJANGO_SETTINGS_MODULE'] = "settings"
 
define('port', type=int, default=8888)
 
class HelloHandler(tornado.web.RequestHandler):
	def get(self):
		self.write('Hello from tornado')

def main():
	"""
	Single threaded WSGI is running as a blocking application and will not magically be running asynchronously.
	So, when Django is handling a request there is no ability to handle another request at the same time within Django.
	You would need to have multiple Tornado instances to handle concurrent requests.
	You certainly can't make use of Tornado's direct asynchronous programming API in Django.
	Thus there isn't really any great benefit from using Tornado with Django via the WSGI interface.
	"""
	parse_command_line()
 
	wsgi_app = tornado.wsgi.WSGIContainer(
		django.core.handlers.wsgi.WSGIHandler())
 
	tornado_app = tornado.web.Application([
		('/hello-tornado', HelloHandler),
		('.*', tornado.web.FallbackHandler, dict(fallback=wsgi_app)),
		])
	server = tornado.httpserver.HTTPServer(tornado_app)
	server.listen(options.port)
	tornado.ioloop.IOLoop.instance().start()
 
if __name__ == '__main__':
	main()
