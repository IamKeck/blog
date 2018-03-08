# -*- coding: utf-8 -*-
from requests_oauthlib import OAuth1Session
import os
import boto3
from boto3.dynamodb.conditions import Key, Attr

BASE_URL = "http://blog.keckserver.xyz/posts/"
TWITTER_URL = "https://api.twitter.com/1.1/statuses/update.json"

def make_tweet(filenames):
    urls = [BASE_URL + filename for filename in filenames]
    return "new article!\n" + "\n".join(urls)


def lambda_handler(event, context):
    filenames = (record["s3"]["object"]["key"].replace("posts/", "") for record in event["Records"])
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table("tweeted_posts")
    new_files = [filename for filename in filenames if len(table.query(KeyConditionExpression=Key("article_name").eq(filename.replace(".html", "")))["Items"]) < 1]
    if len(new_files) > 0:
        twitter = OAuth1Session(os.environ["COMSUMER_KEY"],
                                os.environ["COMSUMER_SECRET"],
                                os.environ["ACCESS_TOKEN"],
                                os.environ["ACCESS_TOKEN_SECRET"])
        twitter.post(TWITTER_URL, {"status": make_tweet(new_files)})
    for new_file in new_files:
        table.put_item(Item={"article_name": new_file.replace(".html", "")})


   


