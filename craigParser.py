from BeautifulSoup import BeautifulSoup
import re
import urllib 

class CraigsParser:
    """ Awesome functions to scrape data from CraigsList"""
    def __init__(self, url):
    	self.url = url
    		
    def getTitle(self):
        """ Gets the title from the post returns str """
    	craigDoc = urllib.urlopen(self.url)
    	craigSoup = BeautifulSoup(craigDoc)
    	title = craigSoup.html.body.h2.prettify()
    	return title
    def getContent(self):
        """ Gets the content from the post returns str """
    	craigDoc = urllib.urlopen(self.url)
    	craigSoup = BeautifulSoup(craigDoc)
        userbody = craigSoup.findAll('div', id="userbody")
        userbodySTR = userbody[0].prettify() # May not be necessary refactor.
        content = userbodySTR.split("<!--")[0] #could use something more elegant...
    	content = re.sub('<div id="userbody">', '', content) #specially this.
    	return content
