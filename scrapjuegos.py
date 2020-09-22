import pymongo
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json


###API ########################
ckey = "y2qkaptwdmuEenoMCMdfESPSi"
csecret = "o4LnW4qRkBFOA4VOz02zWuiB7jWAulIEYWJyYZSvaX7WXdpad4"
atoken = "1168602791897718787-g83FUQ8B0VZsprFwRTrrlL0NnpKnxb"
asecret = "ZUmJWrsBVf0i2HWYMsFXwxInZmZsUmjJ5Ilf6BF0MWqR1"
#####################################

class StdOutListener(StreamListener):
    
    def on_data(self, data):
        dictTweet = json.loads(data)
        try:
            dictTweet["_id"] = str(dictTweet['id'])
            doc = mycol.save(dictTweet)
            print ("SAVED" + str(doc) +"=>" + str(data))
        except:
            print ("Already exists")
            pass
        return True
    
    def on_error(self, status):
        print (status)
        
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, StdOutListener())

'''========mongodb'=========='''
db = pymongo.MongoClient("mongodb://localhost:27017/")
try:
    mydb = db['twitter5']
    mycol = mydb['candidatos']
except:
    mydb = db['twitter5']
    mycol = mydb['candidatos']

'''===============LOCATIONS=============='''    
#twitterStream.filter(locations=[-92.21,-5.02,-75.19,1.88])  
twitterStream.filter(track=["canditados ecuador","politicos","asambleistas ecuador","prefectos ecuador","pulso politico ecuador"
    "presidentes ecuador","alcaldes ecuador"])