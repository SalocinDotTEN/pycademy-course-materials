from mailer import Mailer, Message
import sqlite3
import os, re

PATH = os.getcwdu()

#create database and users table
conn = sqlite3.connect(PATH + r'\profile.db')

##If you want to be with MySQL the only change you have to do is library name, other parts would be exactlly the same!
#import MySQLdb
#cobb = MySQLdb.connect(host = 'localhost', user = 'root', passwd = "YOURPASSWORD")

conn.row_factory = sqlite3.Row
cursor = conn.cursor()
#cursor.execute('drop table IF EXISTS users;')
cursor.execute('''create table IF NOT EXISTS users
                                 (  usid integer primary key autoincrement,
                                    email varchar(100) not null,
                                    password varchar(100) not null,
                                    gender varchar(10) not null,
                                    description varchar(100),
                                    interests varchar(100));''')
conn.close()

class Profile:
    def __init__(self, email, password, gender = "female",
                     description = "", interests = []):
        self.email = email
        self.__password = password
        self.gender = gender
        self.description = description
        self.interests = interests

    @property
    def PSWD(self): return self.__password

    def register(self):
        conn = sqlite3.connect(PATH + r'\profile.db')
        cursor = conn.cursor()
        cursor.execute('select count(*) from users where email = "%s"' % self.email)
        if cursor.fetchone()[0] > 0:
            return False
        cursor.execute('''insert into users
                             (email, password, gender, description, interests)
                             values ("{email}", "{password}", "{gender}",
                             "{description}", "{interests}")'''.format(
                             email = self.email, password = self.__password,
                             gender = self.gender, description = self.description,
                             interests = ','.join(self.interests) ))
        conn.commit()
        conn.close()
        return True
        pass

    @staticmethod
    def load_profile(email):
        conn = sqlite3.connect(PATH + r'\profile.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute('select * from users where email = "%s"' % email)
        if cursor.rowcount != 0:
            rec = cursor.fetchone()
            temp = Profile(
                rec['email'],
                rec['password'],
                rec['gender'],
                rec['description'],
                rec['interests'].split(','))
            return temp
        return None

    def __str__(self):
        return str(self.__dict__)
        pass

    def __repr__(self):
        return str(self.__dict__)
        pass

    def send_email(self, subject, body, From = "PyCademy :: Hossein"):
        msg = Message(To = self.email, From = From, Subject = subject, Html = body , )
        sender = Mailer(host = "smtp.gmail.com", use_tls = True,
                             port = 587, usr = "nicolas.yip@tricorsenedi.com", pwd = "ZoiY.82-Zw")
        sender.send(msg)
        pass

#do in interpreter
hosProfile = Profile(email = "nicolas.yip@tricorsenedi.com" , password = "123456")
hosProfile.register()
print hosProfile.PSWD
name = raw_input("Your Name?")
Profile.load_profile("nicolas.yip@tricorsenedi.com").send_email(
    'PyCademy Test for OOP Code', 'Hi! this is a test',
     From = "PyCademy :: " + name)