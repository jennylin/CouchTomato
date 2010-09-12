from craigParser import CraigsParser
from challenge.models import Item
from challenge.models import ItemContact
from challenge.models import ItemDescription
from challenge.models import ItemPicture
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
    def search(self):
        return getResults("http://"+self.craigLoc+".craigslist.org/search/?query=" + self.term +"&catAbb=sss")
    def searchCategory(self, category):
        return getResults("http://"+self.craigLoc+".craigslist.org/search/"+category+"?query="+self.term)
    def getResults(self, url):
        craigDoc = urllib.urlopen(url)
        craigSoup = BeautifulSoup(craigDoc)
        listings = craigSoup.findAll("p", {"class":"row"})
        results = []
        for list in listings:
            try:
                itemUrl = list.a['href']
                parsedListing = CraigsParser(itemUrl)
                item = Item()
                item.url = itemUrl
                price = parsedListing.getPrice()
                # we don't want an item if it's not for sale
                # the > actually should work as an alphabetical comparison =)
                if (price.startswith("$") and price > "$0"):
                    price = price.lstrip("$")
                    item.price = int(price);
                    item.title = parsedListing.getTitle()
                    i = Item.objects.filter(price=item.price, title=item.title)
                    if (i.count() == 0):
                        item.save()
                        itemDescription = ItemDescription()
                        itemDescription.description = parsedListing.getContent()
                        itemDescription.item = item
                        itemDescription.save()
                        # couldn't get it to work for some reason so we'll just parse it when we need it
                        #itemContact = ItemContact()
                        #itemContact.email = parsedListing.getEmail()
                        #itemContact.item = item
                        #itemContact.phone = ''
                        #itemContact.name = ''
                        #itemContact.fb_profile = ''
                        #itemContact.save()
                        parsedListing.getPictures(item)
                    # only save if we haven't saved before
                    results.append(item)
            except ValueError:
                print "value error"
        return results
