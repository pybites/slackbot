import os
import re
import sys

import requests

HTML = 'authors.html'
SITE = 'http://pybit.es'
URL = '{}/{}'.format(SITE, HTML)

NUM_POSTS = re.compile(
    r'<a href="%s/author/[^"]+">\w+</a>\s\((\d+)\)'
    % SITE)

def get_num_posts():
    html = requests.get(URL).text
    num_posts = sum(int(num) for num in NUM_POSTS.findall(html))
    return '{} has {} posts'.format(SITE, num_posts)
