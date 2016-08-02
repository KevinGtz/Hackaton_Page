import os
import webapp2
from webapp2_extras import jinja2

class BaseHandler(webapp2.RequestHandler):
    def render_template(self, template_name):
        renderer = jinja2.get_jinja2(app=app)
        template = renderer.render_tamplate(template_name)
        self.response.write(template)


class MainHandler(BaseHandler):
    def get(self):
        self.render_template('landing.html')


app = webapp2.WSGIApplication([
    webapp2.Route(r'/',
                  handler=MainHandler,
                  name='MainHandler',
                  methods=['GET']),
], debug=True)
