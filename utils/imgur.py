import os
import urllib
import re
import requests


from bs4 import BeautifulSoup
import mkdir

def downloadImage(url, filename):
    path = './img'
    mkdir.make(path)
    response = requests.get(url)
    if response.status_code == 200:
        print('Downloading %s...' % filename)
        with open(os.path.join(path,filename), 'wb') as fo:
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

def verifyImgur(url):
    if 'i.imgur' in url:
        filename = getFilename(url)
        print("Downloading {0} | {1}".format(url, filename))
        downloadImage(url, filename)
    else:
        imageUrl = getImageUrl(url)
        filename = getFilename(imageUrl)
        print("Downloading {0} | {1}".format(imageUrl, filename))
        downloadImage(imageUrl, filename)


raw_urls = ['https://imgur.com/a/y1rF3','https://imgur.com/gallery/HOVt6','http://i.imgur.com/pwmBfC2.jpg',
        'http://imgur.com/CCB3LXA']

for url in raw_urls:
    #image_url = getImageUrl(raw_url)
    #print(image_url)
    #filename = getFilename(image_url)
    #print(filename)
    #downloadImage(image_url, filename)
    print("Getting {0}".format(url))
    verifyImgur(url)
