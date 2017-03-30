import random
import re

import requests

li = re.compile(r'<li>\b(\w+)\b</li>')

URL = 'http://examples.yourdictionary.com/mood-examples.html'

html = requests.get(URL).text.lower()
all_moods = li.findall(html)

def get_mood():
    mood = random.choice(all_moods)
    return 'Yo Dog, today I feel {}'.format(mood)


if __name__ == '__main__':
    print('Getting 3 random moods for our bot: ')
    for i in range(3):
        print(get_mood())
