# -*- coding: utf-8 -*-
import twitter
import json

f=open("Twitter_token.json",'r')
jt=json.load(f)

api=twitter.Api(consumer_key=jt["consumer_key"],
                consumer_secret=jt['consumer_secret'],
                access_token_key=jt['access_token_key'],
                access_token_secret=jt['access_token_secret'])

api.VerifyCredentials()
s=api.GetSearch('bahubali')
for tweet in s:
    print(tweet.text)
    
