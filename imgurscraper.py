#!/bin/python
import string
import random
import urllib

def id_generator(size=7, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):

    identity =  ''.join(random.choice(chars) for _ in range(size))
    
    print identity

    picture = urllib.URLopener()
    try:
        picture.retrieve("http://i.imgur.com/%s.png" % identity, "%s.png" % identity)
        print "Downloaded %s.png" % identity
    except:
        pass


print "How many images do you want to try and download?"
ans = raw_input(">>>   ")


for x in range(0,int(float(ans))):
    id_generator()

    


