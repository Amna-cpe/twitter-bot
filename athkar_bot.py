JSON_ATHKAT = 'https://www.hisnmuslim.com/api/ar/27.json'
import json
import tweepy
from os import environ
import time
import schedule
import traceback



API_KEY=environ['API_KEY']
API_SECRET= environ['API_SECRET']
ACCESS_TOKEN  = environ['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = environ['ACCECC_TOKEN_SECRET']


auth = tweepy.OAuthHandler(API_KEY , API_SECRET)
auth.set_access_token(ACCESS_TOKEN , ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)
        
 # print all of the contetnts every 5pm and 5 am
def Get_All_Athkar():
    with open('athkar.json', encoding="utf-8") as f:
        data = json.load(f)    
    for i in data:   
        tweet =i['ARABIC_TEXT']           
        api.update_status(tweet[0:240],tweet_mode='extended')


 

def batch_delete():  
  
    for status in tweepy.Cursor(api.user_timeline).items():
        try:
            api.destroy_status(status.id)
            print("Deleted:", status.id)
        except Exception:
            traceback.print_exc()
            print("Failed to delete:", status.id)

def job():
    Get_All_Athkar()   
    print("I'm working...")


# 1:30 pm
schedule.every().day.at("10:30").do(job) 
# 1:30 am
schedule.every().day.at("01:30").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)





