# coding: utf-8
'''
import urllib


def GetURL(url):
    s = 'error'
    try:
        f = urllib.urlopen(url)
        s = f.read()
    except Exception as e:
        s = 'error: {}'.format(e)

    return s

url = 'http://yandex.ru'
print GetURL(url)

from requests import request

t = request('GET', 'http://rambler.ru').text
with open('test.html', 'w', encoding='utf-8') as f:
    f.write(t)

import urllib2
import pprint
url = "https://vk.com/topic-142009231_35086172"
url = "https://vk.com/topic-142009231_35086172"
f = urllib2.urlopen(url)
content = unicode(f.read(), 'cp1251')
print content
'''


'''
from bs4 import BeautifulSoup

file = r"data/view-source_https___vk.com_topic-142009231_35086172.html"
content = []
with open(file) as f:
    for line in f.readlines():
        content.append(line)

for l in content:
    print l
    soup = BeautifulSoup(l, "html.parser")
    data = soup.findAll('html-attribute-name')
    print data
'''

import requests

headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
      }

user_id = 12345
url = 'http://www.kinopoisk.ru/user/%d/votes/list/ord/date/page/2/#list' % (user_id) # url для второй страницы
url = "https://vk.com/topic-142009231_35086172"
r = requests.get(url)
with open('test.html', 'w') as output_file:
  output_file.write(r.text.encode('cp1251'))