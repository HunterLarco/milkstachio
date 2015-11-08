import webapp2
from google.appengine.ext.webapp import template
import os


from lib import api
from lib.models import *


class APIHandler(api.RequestHandler):
  ERROR_MAP = []
  
  
class MainHandler(webapp2.RequestHandler):
  def get(self):
    template_values = {}
    path = os.path.join(os.path.dirname(__file__), 'pages/main.html')
    self.response.out.write(template.render(path, template_values))
    

app = webapp2.WSGIApplication([
  ('/api(?:/.*)?', APIHandler),
  ('.*', MainHandler)
], debug=True)