#!/bin/python
import string
import random

def id_generator(size=7, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):

    identity =  ''.join(random.choice(chars) for _ in range(size))

    print identity

id_generator()

#TODO: save file from site, check for jpg and png


