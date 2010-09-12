from BeautifulSoup import BeautifulSoup
from challenge.models import ItemPicture
import re
import urllib 

class CraigsParser:
    """ Awesome functions to scrape data from CraigsList"""
    def __init__(self, url):
    	craigDoc = urllib.urlopen(url)
    	self.craigSoup = BeautifulSoup(craigDoc)
    		
    def getPrice(self):
        """ Gets the title from the post returns str """
    	price = self.craigSoup.html.body.h2.contents[0].lstrip(" ")
        try:
            price = price.split(" - ")[1]
            price = price.split(" ")[0]
        except IndexError, e:
            return "-1" # means item is not for sale
        return price
    def getTitle(self):
        """ Gets the title from the post returns str """
    	title = self.craigSoup.html.body.h2.contents[0].split(" - ")[0]
    	return title
    def getContent(self):
        """ Gets the content from the post returns str """
        userbody = self.craigSoup.findAll('div', id="userbody")
        userbodySTR = userbody[0].prettify() # May not be necessary refactor.
        content = userbodySTR.split("<!--")[0] #could use something more elegant...
    	content = re.sub('<div id="userbody">', '', content) #specially this.
    	return content
    def getPictures(self, item):
        pictures = self.craigSoup.findAll("img")
        for pic in pictures:
            item_pic = ItemPicture()
            item_pic.item = item
            item_pic.pic = pic
