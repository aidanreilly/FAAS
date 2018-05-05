import webapp2
import urllib2
class HourCronPage(webapp2.RequestHandler):
    def get(self):
        request = urllib2.Request('https://us-central1-go-fibonacci.cloudfunctions.net/http', headers={"cronrequest" : "true"})
        request2 = urllib2.Request('https://us-central1-go-fibonacci-recur.cloudfunctions.net/http', headers={"cronrequest" : "true"})
        contents = urllib2.urlopen(request).read()
        contents2 = urllib2.urlopen(request2).read()
app = webapp2.WSGIApplication([
    ('/hour', HourCronPage),
    ], debug=True)