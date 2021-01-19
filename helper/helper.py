
import pyshorteners     #for shortening Url's
import re   #For regex Operations
from config import Config
import requests
import json
from spellchecker import SpellChecker
from random import randint
import string

def passgen(length,symbol,number) :

    try:
        length = int(length)
    except:
        return False

    letters = string.ascii_letters
    numbers = ''
    symbols = ''
    if number :
        numbers = string.digits
    if symbol :
        symbols = string.punctuation
    all_chars = list(letters+numbers+symbols)
    password = ''
    for i in range(int(length)) :
        password += all_chars[randint(0,len(all_chars)-1)]

    return password


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

def get_info(id) :

    API_KEY = Config.API_KEY
    url = 'http://www.omdbapi.com/'
    params = {'apikey':API_KEY, 'i':id}
    res = requests.get(url, params=params)
    if res.status_code != 200 :
        return {'error':'Either apikey is void or Try after some timw!'}
    resp = json.loads(res.text)
    if resp['Response'] == 'False' :
        return {'error':resp['Error']}
    else :
        return resp


def spellcorrect(para) :

    spell = SpellChecker()
    if len(para) == 0 :
        return para
    para_list = para.split(' ')
    misspelled = spell.unknown(para_list)
    corrected = ''
    for word in para_list :
        if word in misspelled :
            corrected += spell.correction(word)
        else :
            corrected += word
        corrected += ' '

    return corrected
