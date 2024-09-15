import glob, os
from PIL import Image
from mailer import Message, Mailer

files = glob.glob('*_small.png')
for fn in files:
    os.remove(fn)

files = glob.glob('*.jpg')

for fn in files:
    img = Image.open(fn)
    img.thumbnail( (600, 600), Image.ANTIALIAS )
    img.save(os.path.splitext(fn)[0] + '_small.png', 'PNG')

files = glob.glob('*_small.png')
msg = Message(To = 'khcc@kharazmisoft.com', From = "PyCon", Subject = "Check Images",
            Html = "Wow nice <b>small</b> images", attachments = files[:3] )
sender = Mailer(host = "smtp.gmail.com", use_tls = True,
                     port = 587, usr = "hossein@pycademy.net", pwd = "pycademy")
sender.send(msg)

