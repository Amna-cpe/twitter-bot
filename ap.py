import tweepy
import requests
import os
from os import environ
import random
import json
import time
import schedule
import io

API_KEY="0MCB7k7WapRFQ4cELARnmK9T4"
API_SECRET= "L3YX4CnZFoyMFyepIjP65GyUfyDjGXsRkNeMfNB35vkdEtB1wt"
ACCESS_TOKEN  = "1349122191040905223-DvYa0ei0ie3uuc01mQoheCGebWOeGm"
ACCESS_TOKEN_SECRET = "kfWkSyiz6Jv1sLpRR9DfMBBptCiEnRzhuHfq3OuL8WJ8B"

 def sendMail(name, email, msg):

    accesToken =  oAuthClient.getAccessToken();

    transport = nodemailer.createTransport({
    service: "gmail",
    auth: {
    type: "OAuth2",
    user: "amna.the.nerdy@gmail.com",
    clientId: CLIENT_ID,
    clientSecret: CLIENT_SECRET,
    refreshToken: REF_TOKEN,
    accessToken: accesToken,
    },
    });

     mailOptions = {
    from: `${name}`,
    to: "amna.the.nerdy@gmail.com",
    subject: "from portfolio",
    html: `<p>from:${email} <br> ${msg}</p>`,
    };

     result =  transport.sendMail(mailOptions);

    return result;
 






auth = tweepy.OAuthHandler(API_KEY , API_SECRET)
auth.set_access_token(ACCESS_TOKEN , ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)


#Add the user Id you want to get tweets
user_id="rh11e0"
#Add the number of tweets you want to get
number_of_tweets= 10

#count: maximum allowed tweets count
#tweet_mode: extended to get the full text,it prevents a primary tweet longer than 140 characters from being truncated.

timeline = api.user_timeline(screen_name=user_id,count=number_of_tweets,tweet_mode="extended")

# Iterate and print tweets
# textonly_tweets = [`https://twitter.com/twitter/statuses/${tweet.id}` for tweet in timeline]

with io.open("test.txt", "w", encoding="utf-8") as f:
    for tweet in timeline:
        f.write("https://twitter.com/twitter/statuses/"+str(tweet.id)+"\n\n")
        
# print(*textonly_tweets, sep = "\n")


