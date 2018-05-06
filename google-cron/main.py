import webapp2
import urllib2
class HourCronPage(webapp2.RequestHandler):
    def get(self):
        requestg = urllib2.Request('https://us-central1-go-fibonacci.cloudfunctions.net/http', headers={"cronrequest" : "true"})
        requestgr = urllib2.Request('https://us-central1-go-fibonacci-recur.cloudfunctions.net/http', headers={"cronrequest" : "true"})
        request_az = urllib2.Request('https://calfibonaccirecur.azurewebsites.net/api/calcFibonacci', headers={"cronrequest" : "true"})
        request_azr = urllib2.Request('https://calfibonaccirecur.azurewebsites.net/api/calcFibonacci', headers={"cronrequest" : "true"})
        request_a = urllib2.Request('https://g8h74so6w0.execute-api.us-east-1.amazonaws.com/dev/ping', headers={"cronrequest" : "true"})
        request_ar = urllib2.Request('https://k9kec8cpgc.execute-api.us-east-1.amazonaws.com/dev/ping', headers={"cronrequest" : "true"})

        contents_g = urllib2.urlopen(request_g).read()
        contents_gr = urllib2.urlopen(request_gr).read()
        contents_az = urllib2.urlopen(request_az).read()
        contents_azr = urllib2.urlopen(request_azr).read()
        contents_a = urllib2.urlopen(request_a).read()
        contents_ar = urllib2.urlopen(request_ar).read()
app = webapp2.WSGIApplication([
    ('/hour', HourCronPage),
    ], debug=True)