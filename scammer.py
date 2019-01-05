import random
import os
import string
import json
import requests

chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed(os.urandom(1024))

url = 'https://www.instagram.com'

names = json.loads(open('names.json').read())

for name in names:
    name_extra = ''.join(random.choice(string.digits))

    username = name.lower() + name_extra + '@yahoo.com'
    password = ''.join(random.choice(chars) for i in range(8))

    requests.post(url, allow_redirects=False, data= {
        'A2sksfsmKfOskfmzkvnAo4fdnf' : username,
        'PdfngnDFn1ddwec7molokcvwrf' : password
    } )

print('sending username %s and password %s' % (username, password))