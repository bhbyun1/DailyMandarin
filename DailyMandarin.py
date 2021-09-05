import tweepy
import codes
from bs4 import BeautifulSoup
import time

codes.init()

URL = "https://www.transparent.com/word-of-the-day/today/chinese.html"

codes.driver.get(URL)

time.sleep(15)

html = codes.driver.page_source
soup = BeautifulSoup(html, "html.parser")

# print(codes.API)
# print(codes.APISecret)
# print(codes.BearerToken)

auth = tweepy.OAuthHandler(codes.API, codes.APISecret)
auth.set_access_token(codes.AccessToken, codes.AccessTokenSecret)
api = tweepy.API(auth)
api.update_status("Hello world")