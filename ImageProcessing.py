#image downloading from a url
# 19th jul 2020
# Manas Dash
import requests

# download image
r = requests.get('https://www.python.org/static/img/python-logo@2x.png')
with open('python_logo.png', 'wb')as f:
    f.write(r.content)
