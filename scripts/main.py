
import requests
'''
def hello():
    print("Hello world !!\n")
    x = requests.get('https://github.com/theabmitra')
    print(x.text)

if __name__ == "__main__":
    hello()
'''
from BeautifulSoup import BeautifulSoup
import sys
import urllib2
import re
import json

#Ask for movie title
title = "One Flew Over the Cuckoo's Nest"

#Ask for which year
year = "1975"

#Search for spaces in the title string
raw_string = re.compile(r' ')

#Replace spaces with a plus sign
searchstring = raw_string.sub('+', title)

#Prints the search string
print searchstring

#The actual query
url = "http://www.imdbapi.com/?t=" + searchstring + "&y="+year

request = urllib2.Request(url)

response = json.load(urllib2.urlopen(request))

print json.dumps(response,indent=2)

#if __name__ == "__main__":
