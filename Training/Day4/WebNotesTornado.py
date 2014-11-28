'''
Created on 27 Nov 2014

@author: b8605521
'''

import tornado.ioloop
import tornado.web

# a listener
class HelloWorldHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello world")

#manually building routing table
application = tornado.web.Application([
    (r'/', HelloWorldHandler),
])

if __name__ == '__main__':
    application.listen(5000)
    tornado.ioloop.IOLoop.instance().start()