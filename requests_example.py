import requests

# download image
r = requests.get('https://imgs.xkcd.com/comics/python.png')
# with open('comic.png', 'wb')as f:
#     f.write(r.content)
print(r.status_code)
print(r.headers)
print(r.ok)
print(r.url)

payload = {'page':2, 'count':25}
r = requests.get ('https:/httpbin.org/get', params =payload)
print(r)