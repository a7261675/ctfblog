import requests

import urllib.request

rotimi = urllib.request.urlopen("http://shattered.io/static/shattered-1.pdf").read()[:500]

letmein = urllib.request.urlopen("http://shattered.io/static/shattered-2.pdf").read()[:500]

r = requests.get('https://quiz.zoolab.org:32670', params={'username': rotimi, 'password': letmein})

print (r.text)
