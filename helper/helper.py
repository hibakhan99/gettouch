
import pyshorteners     #for shortening Url's
import re   #For regex Operations


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
