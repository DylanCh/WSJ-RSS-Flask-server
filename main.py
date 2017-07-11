import json
import feedparser
import requests
from newsitems import newsitems
import sys, traceback

url = 'http://www.wsj.com/xml/rss/3_7455.xml'

def getFeedWithRequest():
  r = requests.get(url)
  return r

def getFeed():
  r = feedparser.parse(url)
  items = r['items']
  return items

def getRawFeed():
    r = feedparser.parse(url)
    return r

def parseFeed() :
    items = getFeed()
    nItems = []
    for item in items :
        tempItem = newsitems(item.title, item.description, item.link)
        nItems.append(tempItem)
    return nItems

def dumpFeedToFile(isRaw,toJSON):
    if isRaw is True:
        data = getRawFeed()
    else:
        data = getFeed()
    #print(data)
    try :
        if toJSON is True:
            with open('data.json','w') as outfile:
                json.dump(data,outfile)
        else:
            with open("Output.txt", "w") as text_file:
                text_file.write(data)
    except TypeError:
        traceback.print_tb(sys.exc_info(), limit=1, file=sys.stdout)



# feed = parseFeed()
# for item in feed:
#     print(item.title + '\n')
#     print(item.description + '\n')
#     print(item.link+'\n')

dumpFeedToFile(isRaw=True, toJSON=False)






#@app.route('/wsj',methods=['GET'])
#def wsj():
#  getFeed()
  
  
