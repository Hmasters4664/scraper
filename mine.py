# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 15:05:52 2018

@author: Olivier
"""

from urllib.request import urlopen as uReq
from urllib.request import Request
import urllib.request
from bs4 import BeautifulSoup as soup

url_="https://www.whatsonincapetown.com/post/dreamland-kirsten-beets-salon-91/"
my_url= url_



req = Request(my_url,headers={'User-Agent': 'Mozilla/5.0'})
uclient=uReq(req)

page_html = uclient.read()

uclient.close()

Page_soup =soup(page_html, "html.parser") # hrml parser

Page_soup.find_all('p')[2].get_text()
Page_soup.find_all('p')[2].find_next_sibling().get_text()