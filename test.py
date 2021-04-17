# -*- coding: utf-8 -*-
"""test.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oykixdYw0aUCv16K-08iIWCptJC3A7Wg
"""
import os
from os import eviron
from requests_html import HTMLSession, AsyncHTMLSession

async def surrender(response):
    something = await response.html.render(scrolldown=1000, sleep=1)
    return something

url = 'https://sport.detik.com/'

try:
    asession = HTMLSession()
    response = asession.get(url)
     
except requests.exceptions.RequestException as e:
    print(e)

artikel = response.html.find('h2')
link = response.html.find('div.desc_nhl a')

for i in range(len(artikel)) : 
  print(artikel[i].text)
  print(link[i].absolute_links)

