import requests
import random

def newsfetcher():
    newslist = dict() #for creating a new json
    #Saving the tags
    sections = ['sport','football','environment','books','music','science','technology','tv-and-radio','artanddesign','film','games','stage','lifeandstyle','fashion','business']
    #Saving URLs to avoid news article duplication
    #urls = []

    for i in range(sections.__len__()):
     r = requests.get(
            'https://content.guardianapis.com/search?q='+sections[i]+'&order-by=newest&api-key=b19ec11d-aa8f-46fe-adac-7c98713ae0b0' + "&format=json")
     data = r.json()

     #urls.append(data["response"]["results"][0]["apiUrl"])
     #print(urls)
     #if(urls.index(data["response"]["results"][0]["apiUrl"])):
      #print("Match")
      #newslist[(data["response"]["results"][random.randint(1,5)]["sectionId"])] = data["response"]["results"][0]["apiUrl"]
     #else:
     newslist[(data["response"]["results"][0]["sectionId"])]= data["response"]["results"][0]["apiUrl"]

    print(newslist)
    return newslist

results = newsfetcher()

import json
with open('initialnewslist.json', 'w') as fp:
    json.dump(results, fp)

newsfetcher()






