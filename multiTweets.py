# dependencies 
import tweepy
import json
import time

# Quotes to Tweet
happy_quotes = [
    "For every minute you are angry you lose sixty seconds of happiness. - Ralph Waldo Emerson",
    "Folks are usually about as happy as they make their minds up to be. - Abraham Lincoln",
    "Happiness is when what you think, what you say, and what you do are in harmony. - Mahatma Gandhi",
    "Count your age by friends, not years. Count your life by smiles, not tears. - John Lennon",
    "Happiness is a warm puppy. - Charles M. Schulz",
    "The happiness of your life depends upon the quality of your thoughts. - Marcus Aurelius",
    "Now and then it's good to pause in our pursuit of happiness and just be happy. - Guillaume Apollinaire"]

# Twitter API Credentials
consumer_key = "nvw0aFUEiWC4uAxzXylujbai8"
consumer_secret = "9nooHblTgmaDU64wGxLs2bfw9lG6zj8qZvxzeHDGvLIZoUB2mB"
access_token = "40598976-5WYNZ8hYe0Le9gqFfKyScapq9v1MsxtY9JbEjlsxp"
access_token_secret = "JRWbqPLCjkvNd55NSTRR8NaHTdCIayQauUO5pAIMaQ3EU"

#Authenticate
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

#Create a function that tweets
def TweetOut(tweetMsg, tweet_number):
    api.update_status(tweetMsg)

def sendMsg(id, msg):
     api.send_direct_message(user=id,text=msg)

# api.send_direct_message(user="fervis_lauan", text="Hey There!")
# # Tweet a random quote
i = 0
for quote in happy_quotes:
    # Call the TweetQuotes function and specify the tweet number
    msg = "Heroku Test " + str(i)
    TweetOut((msg +" " + happy_quotes[i]),i)
    # Once tweeted, wait 60 seconds before doing anything else
    time.sleep(20)
    # Add 1 to the counter prior to re-running the loop
    i+=1

# i=0
# # sendMsg("fervis_lauan","Sending you the message ViA function")
# for users in ["fervis_lauan","afhaque"]:
#     for quote in happy_quotes:
#         # Call the sendMsg function and specify the tweet number
#         #try:
#         sendMsg("fervis_lauan", quote)
#         time.sleep(60)
#         #    i+=1
#         #except:
#         #    print("Done")

