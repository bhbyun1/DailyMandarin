import tweepy
import codes
from bs4 import BeautifulSoup
import time
import schedule

codes.init()
auth = tweepy.OAuthHandler(codes.API, codes.APISecret)
auth.set_access_token(codes.AccessToken, codes.AccessTokenSecret)
api = tweepy.API(auth)

URL = "https://www.chineseclass101.com/chinese-phrases/"

def doScrape():
    codes.driver.get(URL)

    time.sleep(15)

    html = codes.driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    mandarin = codes.driver.find_elements_by_class_name("r101-wotd-widget__word")
    english = codes.driver.find_elements_by_class_name("r101-wotd-widget__english")

    return (mandarin, english)


#print("Word of the day\n" + str(mandarin[0].text) + "\n" + str(english[0].text))

def tweetPost():
    mandarin, english = doScrape()
    message = "Word of the day:\n" + str(mandarin[0].text) + "\n" + str(english[0].text)
    api.update_status(message)

schedule.every().day.at("03:33").do(tweetPost)

while True:
    schedule.run_pending()
    time.sleep(1)