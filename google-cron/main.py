import webapp2
import urllib2
class HourCronPage(webapp2.RequestHandler):
    def get(self):
        #begin google pings
        request_g = urllib2.Request('https://us-central1-go-fibonacci.cloudfunctions.net/http', headers={"cronrequest" : "true"})
        contents_g = urllib2.urlopen(request_g, timeout = 500).read()

        request_gr256 = urllib2.Request('https://us-central1-go-fibonacci-recur.cloudfunctions.net/http', headers={"cronrequest" : "true"})
        contents_gr256 = urllib2.urlopen(request_gr256, timeout = 500).read()

        request_gr512 = urllib2.Request('https://us-central1-go-fibonacci-recur.cloudfunctions.net/http-512', headers={"cronrequest" : "true"})
        contents_gr512 = urllib2.urlopen(request_gr512, timeout = 500).read()

        request_gr1GB = urllib2.Request('https://us-central1-go-fibonacci-recur.cloudfunctions.net/http-1GB', headers={"cronrequest" : "true"})
        contents_gr1GB = urllib2.urlopen(request_gr1GB, timeout = 500).read()

        request_gr2GB = urllib2.Request('https://us-central1-go-fibonacci-recur.cloudfunctions.net/http-1GB', headers={"cronrequest" : "true"})
        contents_gr2GB = urllib2.urlopen(request_gr2GB, timeout = 500).read()

        #begin azure pings. 2 pings only
        request_az = urllib2.Request('https://calfibonacci.azurewebsites.net/api/calcFibonacci', headers={"cronrequest" : "true"})
        contents_az = urllib2.urlopen(request_az, timeout = 500).read()

        request_azr = urllib2.Request('https://calfibonaccirecur.azurewebsites.net/api/calcFibonacci', headers={"cronrequest" : "true"})
        contents_azr = urllib2.urlopen(request_azr, timeout = 500).read()
        
        #Begin AWS. 2 pings only
        request_a = urllib2.Request('https://g8h74so6w0.execute-api.us-east-1.amazonaws.com/dev/ping', headers={"cronrequest" : "true"})
        contents_a = urllib2.urlopen(request_a, timeout = 500).read()

        request_ar256 = urllib2.Request('https://k9kec8cpgc.execute-api.us-east-1.amazonaws.com/dev/ping', headers={"cronrequest" : "true"})
        contents_ar256 = urllib2.urlopen(request_ar256, timeout = 500).read()

        request_ar512 = urllib2.Request('https://0qwlklexf2.execute-api.us-east-1.amazonaws.com/dev/ping', headers={"cronrequest" : "true"})
        contents_ar512 = urllib2.urlopen(request_ar512, timeout = 500).read()

        request_ar1GB = urllib2.Request('https://1fd9j85pbj.execute-api.us-east-1.amazonaws.com/dev/ping', headers={"cronrequest" : "true"})
        contents_ar1GB = urllib2.urlopen(request_ar1GB, timeout = 500).read()

        request_ar2GB = urllib2.Request('https://l1zp09xozj.execute-api.us-east-1.amazonaws.com/dev/ping', headers={"cronrequest" : "true"})
        contents_ar2GB = urllib2.urlopen(request_ar2GB, timeout = 500).read()
        
app = webapp2.WSGIApplication([
    ('/hour', HourCronPage),
    ], debug=True)