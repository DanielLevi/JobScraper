# usr/bin/python
# -*- coding: latin-1 -*-

__author__ = 'Daniel Levi'
#__path__ = '/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages'

from bs4 import BeautifulSoup
from myconfig import *
from twilio.rest import TwilioRestClient
import requests

## set headers, parameters, url for session request
headers = {'User-Agent': 'Mozilla/5.0'}
payload = {'id': 'INSERT_ID_HERE', 'pin': 'INSERT_PIN_HERE', 'location': '', 'qstring': '', 'absr_ID': '', 'foil': '', 'submitLogin': '1'}
url = 'https://aesoponline.com/login.asp?x=x&&pswd=&sso='

## begin session
session = requests.Session()
response = session.get(url, headers=headers)

## get and store cookies
cookies = requests.utils.cookiejar_from_dict(requests.utils.dict_from_cookiejar(session.cookies))

## post url
response = session.post(url, headers=headers, data=payload, cookies=cookies)

## create soup object
soup = BeautifulSoup(response.text)

# parse for alert text
alert = soup.find("a", {"href": "/Substitute/Schedule/AvailableJobs"})
alert = alert.find("span").text

## determine if job available, notify user
if alert != "0":
    client = TwilioRestClient(account=TWILIO_ACCOUNT_SID, token=TWILIO_AUTH_TOKEN)
    message = client.messages.create(to=MY_NUMBER, from_=TWILIO_NUMBER, body="Wakie, Wakie! The early bird gets the worm.")

## For testing --
# else:
#     client = TwilioRestClient(account=TWILIO_ACCOUNT_SID, token=TWILIO_AUTH_TOKEN)
#     message = client.messages.create(to=MY_NUMBER, from_=TWILIO_NUMBER, body="At least it's working...")
