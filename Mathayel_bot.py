import tweepy
import requests
import os
from os import environ
import random
import json
import time
import schedule

API_KEY=environ['API_KEY']
API_SECRET= environ['API_SECRET']
ACCESS_TOKEN  = environ['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = environ['ACCECC_TOKEN_SECRET']

auth = tweepy.OAuthHandler(API_KEY , API_SECRET)
auth.set_access_token(ACCESS_TOKEN , ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

status = "@mathayelMF You can do it you almost there"


def get_random_img():
    with open('data.json') as f:
        data = json.load(f)
    x = random.randint(0,48)
    world = data[x]["image"]
    return world
   

def tweet_with_rand_img(url):
   
    filename = 'temp.jpg'
    request = requests.get(url, stream=True)
    if request.status_code == 200:
        with open(filename, 'wb') as image:
            for chunk in request:
                image.write(chunk)
        status = "@mathayelMF You can do it you almost there"
        api.update_with_media(filename, status)
        os.remove(filename)
    else:
        print("Unable to download image")


url = get_random_img()

def job():
    tweet_with_rand_img(url)
    print("I'm working...")


schedule.every().day.at("10:30").do(job)


while True:
    schedule.run_pending()
    time.sleep(1)





