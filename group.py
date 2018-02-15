# -*- coding: utf-8 -*-
import os
import re
import time
import json
import hashlib
import cookielib
import urllib
import urllib2
import sqlite3
import pickle
from HTMLParser import HTMLParser
import traceback


class parseEudictGroup(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.groupID = []
        self.groupName= []
        self.flag = 0
    def handle_starttag(self, tag, attrs):
        # retrive the terms
        if tag == 'a':
            if attrs[0][0] == 'class' and attrs[0][1] == 'media_heading_a new_cateitem_click' and int(attrs[1][1]) >=0:
                self.flag = 1
                self.groupID.append(attrs[1][1])
    def handle_data(self,data):
        if self.flag:
            self.groupName.append(data)
        self.flag = 0

class parseYoudaoGroup(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.groupName= []
        self.flag = 0
    def handle_starttag(self, tag, attrs):
        # retrive the terms
        if tag == 'select':
            if attrs[0][0] == 'id' and attrs[0][1] == 'select_category':
                self.flag = 1
        if self.flag:
            if tag == 'option':
                if attrs[0][0] == 'value' and attrs[0][1]:
                    self.groupName.append(attrs[0][1])
    def handle_endtag(self,tag):
        if tag == 'select':
            self.flag = 0

with open('eudictexample.html') as f:
    html = f.read()
    parser = parseEudictGroup()
    parser.feed(html)
    print(dict(zip(parser.groupID,parser.groupName)))


with open('youdaoexample.html') as f:
    html = f.read()
    parser = parseYoudaoGroup()
    parser.feed(html)
    print(parser.groupName)
