import os, sys, collections, re, json, io, base64
import numpy as np
import matplotlib
import matplotlib.pyplot as pp
import matplotlib.animation as anim
from mpl_toolkits.basemap import Basemap

#%matplotlib inline

import requests
import bs4
#import IPython.display
import PIL, PIL.Image, PIL.ImageOps,PIL.ImageEnhance

images = requests.get('http://mars.nasa.gov/msl/multimedia/raw',params = {'s':'1460', 'camera':'FHAZ'})
htmlpage = images.text

soup = bs4.BeautifulSoup(htmlpage, 'lxml')

print("==========================================")
for p in soup.map.parents:
    print(p.title)
print("==========================================")
#print(soup.find_all('img'))

imgs=["http://mars.jpl.nasa.gov"+image['src'] for image in soup.find_all('img') if 'Image' in image['alt']]

print(re.sub('-thm','',imgs[0]))