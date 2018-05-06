import webapp2
import urllib2
class HourCronPage(webapp2.RequestHandler):
    def get(self):
        request_g = urllib2.Request('https://us-central1-go-fibonacci.cloudfunctions.net/http', headers={"cronrequest" : "true"})
        contents_g = urllib2.urlopen(request_g, timeout = 500).read()

        request_gr = urllib2.Request('https://us-central1-go-fibonacci-recur.cloudfunctions.net/http', headers={"cronrequest" : "true"})
        contents_gr = urllib2.urlopen(request_gr, timeout = 500).read()

        request_az = urllib2.Request('https://calfibonacci.azurewebsites.net/api/calcFibonacci', headers={"cronrequest" : "true"})
        contents_az = urllib2.urlopen(request_az, timeout = 500).read()

        request_azr = urllib2.Request('https://calfibonaccirecur.azurewebsites.net/api/calcFibonacci', headers={"cronrequest" : "true"})
        contents_azr = urllib2.urlopen(request_azr, timeout = 500).read()
        
        request_a = urllib2.Request('https://g8h74so6w0.execute-api.us-east-1.amazonaws.com/dev/ping', headers={"cronrequest" : "true"})
        contents_a = urllib2.urlopen(request_a, timeout = 500).read()

        request_ar = urllib2.Request('https://k9kec8cpgc.execute-api.us-east-1.amazonaws.com/dev/ping', headers={"cronrequest" : "true"})
        contents_ar = urllib2.urlopen(request_ar, timeout = 500).read()
        
app = webapp2.WSGIApplication([
    ('/hour', HourCronPage),
    ], debug=True)