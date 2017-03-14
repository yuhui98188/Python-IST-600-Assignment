#importing urllib request package
from urllib import request

#save target link to a vector
url = "http://www.msn.com/en-us/news/world/rabbit-hole-leads-to-incredible-700-year-old-knights-templar-cave-complex/ar-AAnZ8Kg?li=BBnb7Kz"

#reading content on the target webpage by using request function and decode with utf8 format
html = request.urlopen(url).read().decode('utf8')

#type of html
type(html)

#printing html see if url read correctly
print (html[:500])

#import BeautifulSoup from bs4 to analysis structure of the webpage
from bs4 import BeautifulSoup
htmlsoup = BeautifulSoup(html, 'html.parser')
#Ensure html data type
type(htmlsoup)
bs4.BeautifulSoup

#finding first title tag assign to a vector called firsttitle 
firsttitle = htmlsoup.title
firsttitle

#type of firsttitle
type(firsttitle)

#name of the tag for firsttitle
firsttitle.name

#text inside the title tag
firsttitle.get_text()

#finding all instances under "img" tag by using find_all
anchors = htmlsoup.find_all('img')

#type & length of anchors
type(anchors)
len(anchors)

#printing first 8 examples of img tag
print(anchors[:8])

#finding the address of images by searching 'src' tag and convert to string
imgs = [str(img.get('src')) for img in anchors]
len(imgs)

#display first 8 image addresses
imgs[:8]

#focusing on these img addresses start with 'static'
staticimgs = [img for img in imgs if img.startswith('//static')]
len(staticimgs)

#print all img addresses start with static as there are only three addresses
print(staticimgs)
