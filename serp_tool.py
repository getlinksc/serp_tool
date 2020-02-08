import urllib
import urllib.parse
import urllib.request
import json

# change this
ACCESS_KEY = "***REMOVED***"
# change to keywords of interest
KEYWORD = "how to rank instagram"
# change this to the website of interest
WEBSITE = "http://website.to.find" # change this

country = "US"
language = "lang_en"
data = {
    "q" : KEYWORD,
    "country" : country,
    "language" : language
}

# build the url to make request
urlencoded = urllib.parse.urlencode(data)
url = "https://google-search3.p.rapidapi.com/api/v1/search?" + urlencoded
headers = {
    'x-rapidapi-host': "google-search3.p.rapidapi.com",
    'x-rapidapi-key': ACCESS_KEY
}

# create a GET request with the url and headers
req = urllib.request.Request(url, headers=headers)
resp = urllib.request.urlopen(req)
# read the results and parse the JSON
content = resp.read()
results = json.loads(content)

found_in_results = False # keep track if we found the website
for rank, result in enumerate(results):
    title = result['title']
    link = result['link']
    if WEBSITE in link:
        print("Found website at rank: " + str(rank))
        found_in_results = True

if not found_in_results:
    print("Could not find website in search results.")