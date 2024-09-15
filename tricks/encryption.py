import hmac
import string
import hashlib
from Crypto.Cipher import AES
import base64
import random

message = "This is a very private message"
my_private_key = "python is awesome!"

#sha1
t = hmac.new(my_private_key, message, hashlib.sha1 )
print t.hexdigest()

cipher = AES.new(my_private_key, message)
my_private_key = ''.join([random.choice(string.letters + string.digits) for i in range(16)])
cipher.encrypt(message)

message = message + (16 - (len(message) % 16)) * '+'
encrypted_message = base64.b64encode(cipher.encrypt(message))
print encrypted_message
decrypted_message = cipher.decrypt(base64.b64decode(encrypted_message))
print decrypted_message

#EXPLAIN python syntax is one thing and Pythonic development is another thing

##JAVA
##char[] chars = "abcdefghijklmnopqrstuvwxyz".toCharArray();
##StringBuilder sb = new StringBuilder();
##Random random = new Random();
##for (int i = 0; i < 20; i++) {
##    char c = chars[random.nextInt(chars.length)];
##    sb.append(c);
##}
##String output = sb.toString();

##C#
##            char[] chars = new char[62];
##            chars =
##            "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890".ToCharArray();
##            byte[] data = new byte[1];
##            RNGCryptoServiceProvider crypto = new RNGCryptoServiceProvider();
##            crypto.GetNonZeroBytes(data);
##            data = new byte[maxSize];
##            crypto.GetNonZeroBytes(data);
##            StringBuilder result = new StringBuilder(maxSize);
##            foreach (byte b in data)
##            {
##                result.Append(chars[b % (chars.Length)]);
##            }


