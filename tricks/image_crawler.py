import pyquery
from urllib import urlopen
from StringIO import StringIO
from PIL import Image
import uuid
import os

html = urlopen('http://www.bbc.co.uk/').read()
q = pyquery.PyQuery(html)

my_images = [str(q(x).attr('src')) for x in q('img') if q(x).attr('src')[-3:] in ['png', 'gif', 'jpg']]

my_images = [('http://www.bbc.co.uk/'+ x) if x[:4] != 'http' else x for x in my_images]

for link in my_images:
    #get image from web
    try:
        img = Image.open(StringIO(urlopen(link).read()))
        img.save(os.getcwd() + '\\web_img\\' + os.path.basename(link), 'PNG')
    except:
        pass

