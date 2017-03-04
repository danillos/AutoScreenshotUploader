import base64
import requests
import os
from datetime import datetime
os.getcwd()


url = "http://api.imgur.com/3/upload.json"
token = "TOKEN"

os.system('')

filename = datetime.now().strftime('%Y-%m-%d%H:%M:%S')
t = filename + '.png'

os.system('screencapture -i ' + t)
fileadd = os.getcwd() + '/' + t

fh = open(fileadd, 'rb')
base64img = base64.b64encode(fh.read())
os.remove(fileadd)

headers = { 'Authorization': 'Bearer ' + token }
r = requests.post(url, data={'image': base64img}, headers=headers)

link = r.json()['data']['link']

os.system("echo '%s' | pbcopy" % link)

os.system("""
          osascript -e 'display notification "{}" with title "{}"'
          """.format(link, 'Upload successful'))
