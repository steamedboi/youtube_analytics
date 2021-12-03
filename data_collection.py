#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 22:51:32 2021

@author: williamlai
"""

#import libraries
import requests
import pandas as pd
import time

#keys
API_KEY = 'AIzaSyDFqV3TIXtPL74rFxKNfFjZ9x5yZ5VCUC4'
CHANNEL_ID = 'UClPZDGOXuQQBik4OK1GwtbQ'

pageToken = ""
url = 'https://www.googleapis.com/youtube/v3/search?key=' + API_KEY + '&channelId=' + CHANNEL_ID + '&part=snippet,id&order=date&maxResults=10000'+pageToken
response = requests.get(url).json()

print(response)