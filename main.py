import sys
from GUI import GUI
from dotenv import load_dotenv
from os import getenv
import urllib.parse

load_dotenv()
user = int(getenv('user_id'))
tag = urllib.parse.quote(getenv('tag'))
offset = int(getenv('offset'))
limit = int(getenv('limit'))

if __name__ == '__main__':
    if len(sys.argv) > 1:
        try:
            limit = int(sys.argv[1])
        except:
            print('unexpected argument... set limit = 10(default)')
    GUI(user=user, tag=tag, offset = offset, limit=limit)