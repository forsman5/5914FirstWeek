import requests
from requests_oauthlib import OAuth1
import secrets
import json
from ibm_watson import ToneAnalyzerV3

twitterUrl = "https://api.twitter.com/1.1/search/tweets.json"

headeroauth = OAuth1(secrets.consumer_api_key, secrets.consumer_api_secret,
                     secrets.access_token, secrets.access_token_secret,
                     signature_type='auth_header')

tone_analyzer = ToneAnalyzerV3(
    version='2017-09-21',
    iam_apikey= secrets.iam_apikey,
    url='https://gateway.watsonplatform.net/tone-analyzer/api'
)

# return a list of tweet texts
def getData(searchTerm):
    querystring = {"q": searchTerm}

    response = requests.get(twitterUrl, auth=headeroauth, params=querystring)

    resultArr = []
    jsonObj = json.loads(response.text)
    for status in jsonObj["statuses"]:
        resultArr.append(status["text"])

    return resultArr

def getInput():
    return input("Enter a term to search for, or \"stop\" to stop: ")

def preprocessInput(data):
    concatenatedString = ""

    for tweet in data:
        concatenatedString += tweet + ".\n"

    return concatenatedString

def performAnalysis(data):
    params = preprocessInput(data)
    tone_analysis = tone_analyzer.tone(
        {'text': params},
        content_type='application/json'
    ).get_result()

    print('Tones perceived for all tweets about given term, with corresponding intensity scores:')
    print('Intensity scores range from 0.5-1')
    for tone in tone_analysis['document_tone']['tones']:
        print('{}: {}'.format(tone['tone_name'], tone['score']))

# main function below
searchTerm = None
while (searchTerm != 'stop'):
    searchTerm = getInput()
    if (searchTerm != 'stop'): performAnalysis(getData(searchTerm))
