import urllib
import urllib2


rotimi = urllib2.urlopen("http://shattered.io/static/shattered-1.pdf").read()[:500];
 
letmein = urllib2.urlopen("http://shattered.io/static/shattered-2.pdf").read()[:500];


params={'username': rotimi, 'password': letmein}

f = urllib2.urlopen(url = 'https://quiz.ais3.org:32670/',data = urllib.urlencode(params) )


print f.read()

