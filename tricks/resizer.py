import glob, os
from PIL import Image
from mailer import Message, Mailer
import zipfile
from urllib import urlopen
from StringIO import StringIO


#get image from web
img = Image.open(StringIO(urlopen('http://wonderfulengineering.com/wp-content/uploads/2013/11/apple-wallpaper-2.png').read()))
img.thumbnail( (600,600), Image.ANTIALIAS )
img.save(r'apple_small.png', 'PNG')
zipfile.ZipFile("apple.zip", 'a').write('apple.png', 'apple.png')

#extract
zipfile.ZipFile("apple.zip").extractall(path='myimages')

files = glob.glob('*_small.png')
for fn in files:
    os.remove(fn)

#get all JPG files
files = glob.glob('*.jpg')

for fn in files:
    img = Image.open(fn)
    img.thumbnail((600, 600), Image.ANTIALIAS)
    img.save(os.path.splitext(fn)[0] + '_small.png', 'PNG')

files = glob.glob('*_small.png')

zip = zipfile.ZipFile("python.zip", 'a')
for fn in files[:3]:
    zip.write(fn)
zip.close()

msg = Message (To = "tohidi.h@gmail.com", From = "Pycademy",
                Subject = "This is Cool ZIP!!", Html = "Yap!! Really Cool!",
                attachments = ['python.zip'])

sender = Mailer(host = "smtp.gmail.com",
                port = 587,
                use_tls = True,
                usr = "hossein@pycademy.net",
                pwd = "pycademy")
sender.send(msg)