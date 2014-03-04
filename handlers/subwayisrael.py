import os, sys

from BaseHandler import BaseHandler
# from models.models import *

from google.appengine.api.images import get_serving_url

#--------------------------------------------------------------
# MainPage handler
#--------------------------------------------------------------
class MainPage(BaseHandler):

    def get(self):
    	
        self.render("index.html",)
#--------------------------------------------------------------