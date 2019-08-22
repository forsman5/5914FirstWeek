import requests
import secrets

twitterUrl = "https://api.twitter.com/1.1/search/tweets.json"
twitterHeaders = {
    'Authorization': "OAuth oauth_consumer_key=\"" + secrets.oauth_consumer_key + "\",oauth_token=\"" + secrets.oauth_token + "\",oauth_signature_method=\"HMAC-SHA1\",oauth_timestamp=\"1566421117\",oauth_nonce=\"hybzh17hHd7\",oauth_version=\"1.0\",oauth_signature=\"" + secrets.oauth_signature + "\"",
    'User-Agent': "PostmanRuntime/7.15.2",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Host': "api.twitter.com",
    'Cookie': "personalization_id=\"v1_LSWWaiL+qfXS2jo2jEP9tQ==\"; guest_id=v1%3A156633470544492835; lang=en",
    'Accept-Encoding': "gzip, deflate",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
}

def getData(searchTerm):
    querystring = {"q": searchTerm}

    response = requests.request("GET", twitterUrl, headers=twitterHeaders, params=querystring)

    return response.text

def getInput():
    pass

def performAnalysis(data):
    return 'bad'

print(getData("google"))

# main function below
#input = 'google'
#while (input != 'stop'):
#    output = performAnalysis(getData(input))
#    input = getInput()
