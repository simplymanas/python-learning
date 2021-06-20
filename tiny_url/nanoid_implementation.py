import datetime
import time

from nanoid import generate
#
# print(generate()) # => NDzkGoTCdRcaRyt7GOepg
#
# #collision might increase for a lesser size
# print(generate(size=10) )# => "IRFa-VaY2b"
#
# # custome alphabet
# print(generate('1234567890abcdef', 10)) # => "4f9zd13a42"


shortId = generate()

date_value = time.time()
print(date_value)

#datetime stamp
ct = datetime.datetime.now()
print("current time:-", ct)
ts = ct.timestamp()
print(ts)
print(shortId)

#
# [06/04 20:12] McKeating, Richard
# Yes. Tesco own tes.co   and can configure whatever short Url is required .. e.g. https://tes.co/recipefinder     .... but we aim to make Tesco URLs so standard and simple that there is no shortening required.   e.g. tesco.com/clubcard.  (See App and API naming standards)   Names, Rules, re-directions etc for URLs can all be configured in Akamai for Apps ..      (smile)
# (2 liked)
# Recipe Search Engine : What Can I Make With... | Tesco Real Food
# Find recipes by ingredients. Just enter ingredients into our recipe search engine and we'll instantly return a list of tasty recipes for you to enjoy.
# tes.co
#
# [06/04 20:18] McKeating, Richard
# But note - we shouldn't use a tes.co shortening for things that aren't Tesco. If shortening someone else's URL then just use bit.ly. 
# (1 liked)