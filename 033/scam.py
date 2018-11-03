import requests
import os
import random
import string
import json

chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))

url = 'http://craigslist.pottsfam.com/index872dijasydu2iuad27aysdu2yytaus6d2ajsdhasdasd2.php'

names = json.loads(open('names.json').read())

for name in names:
	name_extra = ''.join(random.choice(string.digits))
        if random.randint(1, 3) == 1:
          	username = name.lower() + name_extra + '@yahoo.com'
        if random.randint(1, 3) == 2:
          	username = name.lower() + name_extra + '@gmail.com'
        if random.randint(1, 3) == 3:
          	username = name.lower() + name_extra + '@hotmail.com'
	#uncomment for name only
        #username = name
	password = ''.join(random.choice(chars) for i in range(10))
	requests.post(url, allow_redirects=False, data={
		'USERNAMEFIELD': username,
		'PASSWORDFIELD': password
	})

	print 'sending username %s and password %s' % (username, password)
