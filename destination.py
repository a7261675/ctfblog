#!/usr/bin/python
# -*- coding: utf-8 -*-    
import requests
from bs4 import BeautifulSoup



mainUrl = 'http://www.appledaily.com.tw'
j=0
res = requests.get('https://www.jkforum.net/search.php?mod=forum&searchid=28698&orderby=lastpost&ascdesc=desc&searchsubmit=yes&page=29')

print(res.text)
