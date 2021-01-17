
import pyshorteners     #for shortening Url's
import re   #For regex Operations
from config import Config
import requests
import json

def passgen(length,symbol=True,number=True) :

    return 'abcd'

def shorten_url(url:str) :

    regex = '^http'     #checking if parameter url is actuakky an URL(Regex needs improvement)
    if re.search(regex,url):
        s = pyshorteners.Shortener()
        short_url = s.chilpit.short(url)      #Using chilpit url shortening API
        return short_url
    else :
        return False    #Not a valid URL!

def omdb_search(query,type=False,page=None) :

    API_KEY = Config.API_KEY
    url = "http://www.omdbapi.com/"
    if page :
        query = query.replace(' ','+')
        params = {'s':query, 'apikey':API_KEY,'page':page}
        res = requests.get(url, params=params)
        if res.status_code != 200:
            return {'error':'Either apikey is void or Try after some time!'}
        resp = json.loads(res.text)
        if resp['Response'] == 'False' :
            return {'error':resp['Error']}
        else :
            return resp

    if not type :

        query = query.replace(' ','+')
        params = {'s':query,'apikey':API_KEY}
        res = requests.get(url, params=params)
        if res.status_code != 200:
            return {'error':'Either apikey is void or Try after some timw!'}
        resp = json.loads(res.text)
        if resp['Response'] == 'False' :
            return {'error':resp['Error']}
        else :
            return resp
