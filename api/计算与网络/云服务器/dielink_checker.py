#!/usr/bin/env python
#coding:utf-8
import requests
import urlparse
import sys
import os
import glob


def has_die_link(fd):
    s=fd.read()
    base_url="http://www.qcloud.com"
    import re
    urls_in_markdown = re.findall(r'\[.*?\]\((.*?)\)',s)
    for url in urls_in_markdown:
        full_url = urlparse.urljoin(base_url,url)
        a = requests.get(full_url).text
        print full_url, u'404 - 帮助与文档 - 腾讯云' in a or u'404页面' in a#requests.get(full_url).text


def browse_files(path):
    for f in glob.glob(path + os.sep + '*'):
        print 'f',f
        if os.path.isdir(f):
            print 'ispath'
            for i in  list(browse_files(f)):
                yield i
        else:            
            if f.endswith('.md'):
                yield f

import glob
import os
fns = browse_files('.')
print fns
for fn in fns:
    fd=open(fn)
    print fn,has_die_link(fd)
