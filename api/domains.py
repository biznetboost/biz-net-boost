import json
import logging
import urllib
import urllib2

import webapp2
from google.appengine.api import urlfetch

class CheckAvailability(webapp2.RequestHandler):
	def get(self):
		form_data = json.dumps(["vivekprakash.com", "vivekdeepika.com", "viveksneha.com"])
		print form_data
		url = 'https://api.godaddy.com/v1/domains/available?checkType=FAST'
		headers = {
			'Authorization': 'sso-key dKiNRD95KC3Z_CqGov6kHKpvTRkpL9Fs78L:CqGr1hvKdo97gWvfyfRp8Y',
			'Content-Type': 'application/json',
			'Accept': 'application/json'
		}
		try:
			result = urlfetch.fetch(
				url=url,
				payload=form_data,
				method=urlfetch.POST,
				headers=headers)
			self.response.headers['Content-Type'] = 'text/plain'
			self.response.write(result.content)
		except urlfetch.Error:
			logging.exception('Caught exception fetching url')

app = webapp2.WSGIApplication([
	('/api/domains/available', CheckAvailability),
], debug=True)
