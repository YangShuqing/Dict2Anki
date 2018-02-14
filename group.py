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

    def handle_starttag(self, tag, attrs):
        # retrive the terms
        if tag == 'a':
            for attribute, value in attrs:
                if attribute=='data-id':
                    self.groupID.append(value)

def __getGroups():
    with open('eudictexample.html') as f:
        html = f.read()
        parser = parseEudictGroup()
        parser.feed(html)
        groupID = parser.groupID
        print(groupID)
        groupName = []
        for id in groupID:
            groupName += re.findall(r'data-id="{}">(.*?)</a>'.format(str(id)),html, re.I | re.M)
        return dict(zip(groupID,groupName))
print __getGroups()
