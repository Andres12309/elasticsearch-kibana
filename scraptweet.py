import couchdb
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
            doc = bd.save(dictTweet)
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

'''========couchdb'=========='''
server = couchdb.Server('http://Andres:linuxhack1@localhost:5984/')#entro a cocuhdb con mis credenciales
try:
    bd = server.create('noticias')#ccreo base de datos
except:
    bd = server['noticias']
'''===============LOCATIONS=============='''    
#twitterStream.filter(locations=[-92.21,-5.02,-75.19,1.88])  
twitterStream.filter(track=["EcuavisaInforma","NoticiasUno","NewsHoy","AlertaNewss24",
    "Nort3Noticias","Teleprensa","noticias covid","NewsPapers","eventos"])