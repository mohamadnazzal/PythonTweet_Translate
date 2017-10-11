#to import some tweets in order to translate is :

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time

#************
#to choose a file name and hashtag
hashtag = raw_input("Enter your hashtag: ")

#************

#consumer key, consumer secret, access token, access secret.
ckey="70PuL6cOABrnXWtRaP7xb2L5B"
csecret="Qv0gyS5tdaNbn9SJkbgt2YvnM5XRmm8VXw7gHehufm5olhD9AT"
atoken="215684554-1NXkCgBwnlslCExTsG5xkSNyS01RdcaUy8ApZBVh"
asecret="dwkQfMO6toFgJbIGnbiP2qlVsVQxUoimMy9eILGFW4qx9"
 
class listener(StreamListener):
#count=0
    def on_data(self, data):
 
        #while (count<10):
            #count++;
            tweet_data=data.split(',"text":"')[1]
            tweet_id = data.split(',"text":"')[0]
            print(tweet_data +"\n")
            savefile=str(tweet_data)
            save=open('pizza.txt','a')
            save.write(savefile)
            save.write("\n\n")
            save.close()
            return(True)
 
    def on_error(self, status):
        print (status)
 
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
 
twitterStream = Stream(auth, listener())
twitterStream.filter(track=[hashtag])

