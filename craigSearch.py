from BeautifulSoup import BeautifulSoup
from StringIO import StringIO
import re
import urllib
import simplejson as json
import sys
import math

class CraigsSearch:
    craigsLocations = {"sfbay":(37.413939, -122.149775), "seattle":(47.611937, -122.196330), "washingtondc":(38.898748, -77.037684)}
    def __init__(self, term, location):
    #def __init__(self, term, lat, lng):
        self.term = term
        self.craigLoc = self.getCraigLoc(location)
        #self.craigLoc = getCraigLoc(lat, lng)
    #def getCraigLoc(lat, lng):
    def getCraigLoc(self, location):
        geoInfoStream = urllib.urlopen("http://maps.google.com/maps/api/geocode/json?address="+location+"&sensor=true")
        geoInfo = json.loads(geoInfoStream.read())
        lat1 = geoInfo['results'][0]['geometry']['location']['lat']
        lng1 = geoInfo['results'][0]['geometry']['location']['lng']
        dist = sys.maxint
        craigLoc = ""
        for loc, (lat2, lng2) in self.craigsLocations.items():
           tmp = self.calcDist(lat1, lng1, lat2, lng2) 
           if (tmp < dist):
               dist = tmp
               craigLoc = loc
        return craigLoc
    def calcDist(self, lat1, lng1, lat2, lng2):
        return math.sqrt((lat1-lat2)**2 + (lng1-lng2)**2)
    def getResults(self):
        craigDoc = urllib.urlopen("http://"+self.craigLoc+".craigslist.org/search/?query=" + self.term +"&catAbb=sss")
        craigSoup = BeautifulSoup(craigDoc)
        return craigSoup
