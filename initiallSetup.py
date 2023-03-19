from jsonFunctions import write
import os
from weatherdata import getWeatherData
import json


looping = True
while looping:
    os.system('clear')
    OpenWeatherApi = input("Please enter your open weather API key")
    Town = input("Please enter the town you are using")
    rssLink = input("Please enter your rss news feed link")
    if getWeatherData(OpenWeatherApi, Town) is None:
        print("Please reenter your key and town")
    else:
        looping = False
        ItemsToWrite = {'api': OpenWeatherApi, 'town': Town, 'rssLink':rssLink}
        write(ItemsToWrite, "data.json","w")
        print("Install success")
