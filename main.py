import os.path
import sqlite3

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options

define("port", default=8888, help="run on the given port", type=int)

dbname = "security.db"
conn = sqlite3.connect(dbname)

class IndexHandler(tornado.web.RequestHandler):
	def get(self):
		self.render('idx.html')

class PoemPageHandler(tornado.web.RequestHandler):
	def post(self):
		name = self.get_argument('user')
		password = self.get_argument('password')
		cur = conn.cursor()
		cur.execute("select * from security where name='{}' AND password='{}'".format(name, password))
		user = cur.fetchall()
		if len(user) == 0:
			user.append("認証失敗")
		cur.close()
		self.render('result.html', user=user)

if __name__ == '__main__':
	tornado.options.parse_command_line()
	app = tornado.web.Application(
		handlers=[(r'/', IndexHandler), (r'/result', PoemPageHandler)],
		template_path=os.path.join(os.path.dirname(__file__), "html")
	)
	http_server = tornado.httpserver.HTTPServer(app)
	http_server.listen(options.port)
	tornado.ioloop.IOLoop.instance().start()
