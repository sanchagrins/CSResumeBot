import urllib
import re
import requests
from bs4 import BeautifulSoup

def downloadImage(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        print('Downloading %s...' % filename)
        with open(filename, 'wb') as fo:
            for chunk in response.iter_content(4096):
                fo.write(chunk)

def getImageUrl(raw_url):
    url = raw_url
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

    tags = soup('link')

    for tag in tags:
        link = tag.get('href', None)
        if '/i.imgur' in link:
            return link
        
def getFilename(image_url):
    return re.search(r'(?:[^/][\d\w.]+)+$', image_url).group(0)
    
# ############def 
raw_url = 'https://imgur.com/a/y1rF3'
image_url = getImageUrl(raw_url)
print(image_url)
filename = getFilename(image_url)
print(filename)
downloadImage(image_url, filename)
