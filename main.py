import requests
from requests_oauthlib import OAuth1
import secrets
import json

twitterUrl = "https://api.twitter.com/1.1/search/tweets.json"

headeroauth = OAuth1(secrets.consumer_api_key, secrets.consumer_api_secret,
                     secrets.access_token, secrets.access_token_secret,
                     signature_type='auth_header')

# return a list of tweet texts
def getData(searchTerm):
    querystring = {"q": searchTerm}

    response = requests.get(twitterUrl, auth=headeroauth, params=querystring)

    resultArr = []
    jsonObj = json.loads(response.text)
    print(jsonObj)
    for status in jsonObj["statuses"]:
        resultArr.append(status["text"])

    return resultArr

def getInput():
    return input("Enter a term to search for, or \"stop\" to stop: ")

def performAnalysis(data):
    print(data)

# main function below
searchTerm = None
while (searchTerm != 'stop'):
    searchTerm = getInput()
    if (searchTerm != 'stop'):

        performAnalysis(getData(searchTerm))
