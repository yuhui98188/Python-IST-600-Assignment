#YUHUI ZHONG
#ElemenTree for analyzing child level and grandchild level of a xml modified html site

#importing urllib request package
import urllib.request

#save target link to a vector
url = "http://feeds.washingtonpost.com/rss/politics"

#reading content on the target webpage by using request function and decode with utf8 format
xmlstring = urllib.request.urlopen(url).read().decode('utf8')

#len of xmlstring
len(xmlstring)

#save the target rss web into a xml file and read the path of this file into a vector 
path = '/Users/yzhon_000/Downloads/politics.xml'

#open the file in a write mode
out = open(path, 'w')
out.write(xmlstring)
out.close()

#import ElementTree package, and io package
import xml.etree.ElementTree as etree
import io

#turning the xmlstring into stream for read() function 
xmlfile = io.StringIO(xmlstring)

#create a file by using parse() function which would return the tree structure
tree = etree.parse(xmlfile)
type(tree)

#getting root note
root = tree.getroot()
type(root)

#finding all the links under the main tree
linklist = tree.findall('.//link')
len(linklist)

#print first 10 links
for link in linklist[:10]:
      print(link.text)
      
#access to child level of tree and find its firstchild
firstchild = root[0]

#print the tag for the firstchild
print(firstchild.tag)

#access to grandchild level and print firstgrand's tag, attribute, text
firstgrandchild = firstchild[0]
print(firstgrandchild.tag, firstgrandchild.attrib, firstgrandchild.text)
