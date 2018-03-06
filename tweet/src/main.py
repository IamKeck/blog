# -*- coding: utf-8 -*-
from requests_oauthlib import OAuth1Session
import os

BASE_URL = "http://blog.keckserver.xyz/posts/"
TWITTER_URL = "https://api.twitter.com/1.1/statuses/update.json"

def make_tweet(filenames):
    urls = [BASE_URL + filename.replace("posts/", "") for filename in filenames]
    return "new article!\n" + "\n".join(urls)


def lambda_handler(event, context):
    filenames = [record["s3"]["object"]["key"] for record in event["Records"]]
    twitter = OAuth1Session(os.environ["COMSUMER_KEY"],
                            os.environ["COMSUMER_SECRET"],
                            os.environ["ACCESS_TOKEN"],
                            os.environ["ACCESS_TOKEN_SECRET"])
    twitter.post(TWITTER_URL, {"status": make_tweet(filenames)})


   


